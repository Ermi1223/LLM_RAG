import pinecone
import neo4j
from embedding_utils import EmbeddingHelper
from neo4j_utils import Neo4jHelper

def main():
    # Load environment variables
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # Neo4j and Pinecone setup
    neo4j_helper = Neo4jHelper(os.getenv("NEO4J_URI"), os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
    pinecone_helper = EmbeddingHelper(os.getenv("PINECONE_API_KEY"), os.getenv("PINECONE_ENV"))

    # Fetch data from Neo4j
    data = neo4j_helper.fetch_data()

    # Transform data into embeddings
    embeddings = pinecone_helper.embed_data(data)

    # Upload embeddings to Pinecone
    pinecone_helper.upload_to_pinecone(embeddings)

    # Query Pinecone and Neo4j based on natural language
    user_query = input("Enter a natural language query: ")
    result = pinecone_helper.query_pinecone(user_query)
    print("Pinecone Result:", result)

    # Fetch corresponding data from Neo4j
    cypher_query = nl_to_neoquery(user_query)
    neo4j_result = neo4j_helper.get_data_from_neo4j(cypher_query)
    print("Neo4j Result:", neo4j_result)

def nl_to_neoquery(nl_query):
    # Placeholder function that converts NL query to Cypher query
    if 'find' in nl_query:
        return "MATCH (n:Entity) RETURN n LIMIT 10"
    return "MATCH (n) RETURN n LIMIT 10"

if __name__ == "__main__":
    main()
