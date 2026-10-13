import sys
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# 1. Configure the application
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

from agent import ask_agent


st.set_page_config(
    page_title="AI Business Intelligence Agent",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# 2. Application header
# --------------------------------------------------

st.title("📊 AI Business Intelligence Agent")

st.markdown(
    """
    Ask questions about your e-commerce business using
    natural language.

    **Powered by:** Python · SQLite · ChromaDB · RAG · Ollama
    """
)

st.divider()


# --------------------------------------------------
# 3. Sidebar
# --------------------------------------------------

with st.sidebar:
    st.header("About the Project")

    st.write(
        """
        This AI agent combines structured database queries
        with business document retrieval to answer questions.
        """
    )

    st.subheader("Capabilities")

    st.markdown(
        """
        - SQL-based data analysis
        - Customer and order counts
        - Revenue analysis
        - Payment analysis
        - Business policy search
        - AI-generated explanations
        """
    )

    st.divider()

    st.caption("Model: Llama 3.2:3b")
    st.caption("Runs locally using Ollama")


# --------------------------------------------------
# 4. Example questions
# --------------------------------------------------

st.subheader("Try an example question")

examples = [
    "How many customers are in the database?",
    "What is the total revenue?",
    "How many orders have been delivered?",
    "What does the shipping policy say about delivery dates?",
    "What is the total revenue, and what does the shipping policy say?"
]

selected_question = st.selectbox(
    "Choose a question",
    ["Select an example..."] + examples
)


# --------------------------------------------------
# 5. Question input
# --------------------------------------------------

question = st.text_area(
    "Ask your business question",
    value=(
        selected_question
        if selected_question != "Select an example..."
        else ""
    ),
    placeholder="Example: How many customers are in the database?",
    height=100
)


# --------------------------------------------------
# 6. Generate answer
# --------------------------------------------------

if st.button(
    "Generate Answer",
    type="primary",
    use_container_width=True
):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            with st.spinner(
                "Analyzing database and business documents..."
            ):
                answer = ask_agent(question.strip())

            st.subheader("Analysis Results")

# Split the verified results from the AI explanation
if "### AI Business Explanation" in answer:
    database_part, explanation_part = answer.split(
        "### AI Business Explanation", 1
    )

    st.markdown("### Verified Database Results")

    database_text = database_part.replace(
        "### Verified Database Results", ""
    ).strip()

    st.code(database_text, language="text")

    st.markdown("### AI Business Explanation")
    st.markdown(explanation_part.strip())

else:
    st.markdown(answer)

        except Exception as error:
            st.error(
                "Something went wrong while generating the answer."
            )

            st.code(str(error))


# --------------------------------------------------
# 7. Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI Business Intelligence Agent | "
    "Python + SQL + RAG + Local LLM"
)