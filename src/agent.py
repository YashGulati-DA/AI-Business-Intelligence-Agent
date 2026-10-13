import ollama

from database import run_query
from document_search import search_documents


def ask_agent(question):
    question_lower = question.lower()

    sql_results = "No database query was required."
    document_results = "No documents were required."

    # Determine which information sources are needed
    sql_keywords = [
        "revenue",
        "sales",
        "customer",
        "customers",
        "orders",
        "order",
        "payments",
        "payment",
        "products",
        "categories",
        "delivered",
        "count",
        "total",
    ]

    document_keywords = [
        "policy",
        "refund",
        "shipping",
        "delivery",
        "explain",
        "rules",
        "document",
    ]

    needs_sql = any(
        word in question_lower for word in sql_keywords
    )

    needs_documents = any(
        word in question_lower for word in document_keywords
    )

    # If neither source is identified, use both
    if not needs_sql and not needs_documents:
        needs_sql = True
        needs_documents = True

    # SQL: handle common questions using predefined queries
    if needs_sql:
        if "customer" in question_lower:
            sql = "SELECT COUNT(*) FROM customers"

        elif "revenue" in question_lower or "sales" in question_lower:
            sql = "SELECT SUM(price) FROM order_items"

        elif "payment" in question_lower:
            sql = """
                SELECT payment_type, COUNT(*) AS transaction_count
                FROM payments
                GROUP BY payment_type
                ORDER BY transaction_count DESC
            """

        elif "delivered" in question_lower:
            sql = """
                SELECT COUNT(*) AS delivered_orders
                FROM orders
                WHERE order_status = 'delivered'
            """

        elif "order" in question_lower:
            sql = "SELECT COUNT(*) AS total_orders FROM orders"

        else:
            sql = None

        if sql:
            try:
                columns, rows = run_query(sql)

                # Preserve the actual database results
                sql_results = {
                    "query": sql.strip(),
                    "columns": columns,
                    "rows": rows,
                }

            except Exception as error:
                sql_results = f"SQL execution failed: {error}"

        else:
            sql_results = (
                "No predefined SQL operation matched this question. "
                "A suitable SQL query has not been executed."
            )

    # RAG: retrieve relevant business documents
    if needs_documents:
        try:
            matches = search_documents(question)

            document_results = [
                {
                    "source": item["source"],
                    "text": item["text"],
                }
                for item in matches
            ]

            if not document_results:
                document_results = "No relevant document passages found."

        except Exception as error:
            document_results = (
                f"Document search failed: {error}"
            )

    # Combine the evidence into a business answer
    prompt = f"""
You are an AI Business Intelligence Analyst.

Answer the user's question using only the evidence provided below.

QUESTION:
{question}

DATABASE RESULTS:
{sql_results}

DOCUMENT RESULTS:
{document_results}

RULES:
1. Use only the provided evidence.
2. Never invent numbers, policies, or facts.
3. Do not change or approximate numbers from the database.
4. Explain document information in simple language.
5. Cite document filenames when using document information.
6. If evidence is insufficient, clearly say so.
7. Do not present possible explanations as proven causes.
8. If no SQL query was executed, do not invent database results.
9. Do not claim that a database result proves something it does not.
10. Keep the answer clear and concise.
11. Never rewrite database numbers from memory. Copy every number exactly from the DATABASE RESULTS.
12. If the question asks for a numerical answer, explicitly use the exact value from the database results.

Write a business-friendly answer.
"""

    # Generate the explanation using the local Ollama model
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    ai_answer = response["message"]["content"]

    # Display raw database results separately from the AI explanation
    return (
        "### Verified Database Results\n\n"
        f"```text\n{sql_results}\n```\n\n"
        "### AI Business Explanation\n\n"
        f"{ai_answer}"
    )