import os
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector

# See docker command above to launch a postgres instance with pgvector enabled.
# postgresql://langchain:langchain@localhost:6024/langchain
# docker run --name pgvector-container -e POSTGRES_USER=langchain -e POSTGRES_PASSWORD=langchain -e POSTGRES_DB=langchain -p 6024:5432 -d pgvector/pgvector:pg16
connection = os.environ.get("DATABASE_URL")
if not connection:
    raise ValueError("DATABASE_URL environment variable is not set")


customer_vector_store = PGVector(
    embeddings=OpenAIEmbeddings(),
    collection_name="customers",
    connection=connection,
    use_jsonb=True,
)

COMPANY_DOMAIN = os.environ.get("COMPANY_DOMAIN")
if not COMPANY_DOMAIN:
    raise ValueError("COMPANY_DOMAIN environment variable is not set")


# Define the tools for the agent to use
@tool
def search_tool(query: str):
    """Call this tool to search in customers information"""
    print("Search tool invoked")
    return customer_vector_store.similarity_search(query, k=3)


@tool
def web_search_tool(query: str):
    """Use this tool to search for information on the company's website website. Make sure to pay attention to dates."""
    print("Web search tool invoked")
    web_search = TavilySearchResults(
        name="web_search",
        description="Use this tool to search for information on the company's website. Make sure to pay attention to dates",
        include_domains = [COMPANY_DOMAIN],
        include_images=True,
        max_results=10,
    )
    return web_search.invoke({'query': query})

