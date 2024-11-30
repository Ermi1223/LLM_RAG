import os

class Neo4jConfig:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")  # Default value for local Neo4j
        self.username = os.getenv("NEO4J_USER", "neo4j")  # Default Neo4j username
        self.password = os.getenv("NEO4J_PASSWORD", "your-password")  # Replace with your actual password

    def get_uri(self):
        return self.uri

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

# Usage:
# You can import this class and use its methods wherever you need the Neo4j configuration in your project.
# Example:
# from config.neo4j_config import Neo4jConfig
# neo4j_config = Neo4jConfig()
# print(neo4j_config.get_uri())
