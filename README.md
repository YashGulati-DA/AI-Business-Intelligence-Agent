\# AI Business Intelligence Agent



An AI-powered business intelligence application that combines SQL analytics, Retrieval-Augmented Generation (RAG), semantic document search, and a locally hosted Large Language Model (LLM).



The application allows users to ask business questions in natural language and receive answers using structured database results and retrieved business documents.



\## Features



\- Natural-language business question answering

\- SQL-based customer, order, payment, and revenue analysis

\- Retrieval-Augmented Generation (RAG)

\- Semantic search using Sentence Transformers

\- Vector database using ChromaDB

\- Local LLM integration using Ollama

\- AI-generated business explanations

\- Combined SQL analytics and document retrieval

\- Interactive web interface using Streamlit



\## Technology Stack



\- \*\*Language:\*\* Python

\- \*\*Database:\*\* SQLite

\- \*\*Query Language:\*\* SQL

\- \*\*RAG Framework:\*\* Custom Python implementation

\- \*\*Vector Database:\*\* ChromaDB

\- \*\*Embedding Model:\*\* Sentence Transformers (`all-MiniLM-L6-v2`)

\- \*\*LLM Runtime:\*\* Ollama

\- \*\*Language Model:\*\* Llama 3.2:3b

\- \*\*Frontend:\*\* Streamlit



\## Architecture



1\. The user submits a business question through the Streamlit interface.

2\. The application determines whether database queries, document retrieval, or both are needed.

3\. SQLite executes predefined SQL queries to retrieve structured business data.

4\. Sentence Transformers converts questions and documents into embeddings.

5\. ChromaDB retrieves relevant business documents using semantic similarity.

6\. Ollama generates a natural-language explanation using the available evidence.

7\. Streamlit displays the database results and AI-generated explanation.



\## Example Questions



\- How many customers are in the database?

\- What is the total revenue?

\- How many orders have been delivered?

\- What does the shipping policy say about delivery dates?

\- What is the total revenue, and what does the shipping policy say?



\## Project Structure



```text

AI-Business-Intelligence-Agent/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── data/

│   └── olist.db

├── documents/

│   ├── business\_overview.txt

│   ├── refund\_policy.txt

│   └── shipping\_policy.txt

├── src/

│   ├── agent.py

│   ├── database.py

│   ├── document\_search.py

│   ├── test\_agent.py

│   ├── test\_database.py

│   └── test\_search.py

└── chroma\_db/

```



\## Prerequisites



\- Python 3.10 or a compatible version

\- Ollama

\- Git (optional, for cloning the repository)



\## Installation



\### 1. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd AI-Business-Intelligence-Agent

```



Replace `YOUR\_GITHUB\_REPOSITORY\_URL` with your actual repository URL.



\### 2. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 3. Install the Local Language Model



```bash

ollama pull llama3.2:3b

```



Ensure Ollama is running before launching the application.



\### 4. Configure the Database



Place the required SQLite database at:



```text

data/olist.db

```



The database must contain the tables and columns required by the SQL queries in `src/agent.py`.



\### 5. Run the Application



From the project root, execute:



```bash

python -m streamlit run app.py

```



Open the local URL displayed in the terminal.



\## Dataset and Business Documents



The application uses an SQLite database derived from the Olist Brazilian E-Commerce dataset.



The business policy documents included in this project are example documents created for demonstration purposes. They should not be interpreted as official Olist policies.



The database and generated ChromaDB files are intended to remain local and should not be committed to GitHub.



\## Current Limitations



\- SQL operations use predefined queries rather than dynamically generating SQL for arbitrary questions.

\- Document retrieval depends on the available documents and semantic similarity.

\- The application may occasionally generate inaccurate explanations.

\- Verified database results should be used as the source of truth for numerical answers.

\- Document indexing may need to be refreshed when source documents change.

\- The application is a portfolio prototype and has not been designed for production deployment.



\## Future Improvements



\- Dynamic SQL generation with query validation

\- Improved document chunking and retrieval evaluation

\- More precise document citations

\- Automatic document indexing and refresh

\- Stronger numerical answer validation

\- Query history and user feedback

\- Improved interface and data visualizations



\## Author



Developed as a portfolio project demonstrating practical applications of Python, SQL analytics, Retrieval-Augmented Generation, vector databases, semantic search, and locally hosted Large Language Models.

