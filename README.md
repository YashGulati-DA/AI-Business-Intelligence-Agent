# AI Business Intelligence Agent

An AI-powered business intelligence application that combines **SQL analytics, Retrieval-Augmented Generation (RAG), semantic document search, and a locally hosted Large Language Model (LLM)** to answer business questions using structured data and business documents.

Built with Python, SQLite, ChromaDB, Sentence Transformers, Ollama, and Streamlit, the application enables users to explore e-commerce data and retrieve relevant business information through a natural-language interface.

## Key Features

- **Natural-Language Business Queries:** Ask business questions in plain English.
- **SQL Analytics:** Retrieve customer counts, revenue figures, payment breakdowns, and order statistics using predefined SQL operations.
- **Retrieval-Augmented Generation (RAG):** Combine retrieved business document content with database results.
- **Semantic Document Search:** Find relevant information using Sentence Transformers embeddings.
- **Vector Database:** Store and retrieve document embeddings using ChromaDB.
- **Local LLM Integration:** Generate natural-language explanations using Llama 3.2 through Ollama.
- **Evidence-Based Responses:** Display database results separately from AI-generated explanations.
- **Interactive Web Application:** Submit questions and view results through a Streamlit interface.
- **Local Execution:** Run the language model locally without requiring a paid LLM API.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development and workflow orchestration |
| SQL | Structured data querying and aggregation |
| SQLite | Local relational database |
| Pandas | Data processing where required |
| ChromaDB | Vector storage and semantic retrieval |
| Sentence Transformers | Text embeddings using `all-MiniLM-L6-v2` |
| Ollama | Local LLM execution |
| Llama 3.2:3b | Natural-language explanation generation |
| Streamlit | Interactive web interface |

## System Architecture

The application follows a hybrid SQL and RAG architecture.

1. **User Input:** The user submits a business question through the Streamlit interface.
2. **Question Routing:** Python keyword-based logic determines whether database queries, document retrieval, or both are required.
3. **Structured Data Retrieval:** SQLite executes supported, predefined SQL queries against the e-commerce database.
4. **Document Embedding:** Sentence Transformers converts business documents and questions into vector embeddings.
5. **Semantic Retrieval:** ChromaDB retrieves relevant business documents based on semantic similarity.
6. **LLM Processing:** Ollama runs Llama 3.2 locally to generate a natural-language explanation using the available evidence.
7. **Result Presentation:** Streamlit displays the verified database results separately from the AI-generated explanation.

## Dataset and Demonstrated Results

The application uses an SQLite database derived from the Olist Brazilian E-Commerce dataset.

The following figures were verified during development:

| Metric | Result |
|---|---:|
| Customer records | 99,441 |
| Order records | 99,441 |
| Orders with delivered status | 96,478 |
| Total item-price sum | 13,591,643.70 |
| Business documents indexed | 3 |

**Revenue calculation:** The total item-price sum is calculated using `SUM(price)` from the `order_items` table. It represents the sum of item prices, not total payment value or profit.

**Dataset note:** Customer records are not necessarily the same as unique customers, and order records should not be interpreted as unique purchases beyond the database's actual structure.

## Example Business Questions

The application supports questions such as:

- How many customers are in the database?
- What is the total revenue?
- How many orders have been delivered?
- What does the shipping policy say about delivery dates?
- What is the total revenue, and what does the shipping policy say?

These questions demonstrate structured database querying, semantic document retrieval, and combined SQL-plus-document responses.

## Project Structure

```text
AI-Business-Intelligence-Agent/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
│
├── documents/
│   ├── business_overview.txt
│   ├── refund_policy.txt
│   └── shipping_policy.txt
│
├── src/
│   ├── agent.py
│   ├── database.py
│   ├── document_search.py
│   ├── test_agent.py
│   ├── test_database.py
│   └── test_search.py
│
├── data/                 # Local database; not committed to GitHub
│   └── olist.db
│
└── chroma_db/            # Generated local vector database; not committed
```

## Installation and Setup

### Prerequisites

Before running the application, install:

- Python 3.10 or a compatible version
- Ollama
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/YashGulati-DA/AI-Business-Intelligence-Agent.git
```

Navigate into the project directory:

```bash
cd AI-Business-Intelligence-Agent
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Install the Local Language Model

Download Llama 3.2:3b using Ollama:

```bash
ollama pull llama3.2:3b
```

Ensure Ollama is running before launching the application.

### 4. Configure the Database

Place the required SQLite database at:

```text
data/olist.db
```

The database must contain the tables and columns referenced by the SQL operations in `src/agent.py`.

The database file is excluded from the GitHub repository and must be obtained or configured locally.

### 5. Run the Application

From the project's root directory, execute:

```bash
python -m streamlit run app.py
```

Streamlit will display a local address in the terminal. Open that address in your browser to access the application.

## Document Retrieval

The project currently indexes three example business documents:

- `business_overview.txt` — describes the project's business data and analytical context.
- `refund_policy.txt` — contains example refund-related business rules.
- `shipping_policy.txt` — contains example shipping and delivery information.

Sentence Transformers generates embeddings, and ChromaDB stores the documents for semantic retrieval.

**Important:** These business documents were created as examples for this project. They are not official Olist policies.

## Privacy and Local Execution

- The LLM runs locally through Ollama.
- The application does not require a paid LLM API for its demonstrated workflow.
- The SQLite database is excluded from the public repository.
- The generated ChromaDB directory is excluded from the repository.
- The example business documents and source code are included for project demonstration.

Local execution still depends on the installed software, downloaded model, and correctly configured database.

## Current Limitations

- SQL operations are predefined and selected through keyword-based routing rather than dynamically generated for arbitrary questions.
- The application supports a limited set of analytical queries.
- Semantic retrieval quality depends on document content, embeddings, and similarity ranking.
- The LLM may occasionally produce inaccurate or incomplete explanations.
- Numerical answers should be verified against the displayed database results.
- Document indexing may require refreshing when source documents change.
- The application is a portfolio prototype and has not been designed for production deployment.

## Future Improvements

- Implement dynamic SQL generation with query validation and read-only safeguards.
- Improve question classification and query routing.
- Add more advanced document chunking and retrieval evaluation.
- Display more precise source citations for retrieved passages.
- Automatically refresh the vector database when documents change.
- Strengthen numerical answer validation against SQL results.
- Add query history and user feedback.
- Introduce charts and interactive business dashboards.
- Evaluate answer accuracy using a defined test dataset.

## Skills Demonstrated

- SQL querying and aggregation
- Relational database integration
- Python application development
- Retrieval-Augmented Generation (RAG)
- Vector databases and semantic search
- Text embeddings
- Local LLM integration
- Prompt engineering and evidence-grounded responses
- Streamlit application development
- Data analytics workflow design

GitHub: [YashGulati-DA](https://github.com/YashGulati-DA)

---

This project was developed as a portfolio demonstration of SQL analytics, Retrieval-Augmented Generation, semantic document retrieval, and locally hosted LLM applications.
