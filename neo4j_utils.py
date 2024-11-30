from neo4j import GraphDatabase

class Neo4jHelper:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def fetch_data(self):
        # Example method to fetch data from Neo4j
        with self.driver.session() as session:
            result = session.run("MATCH (n:Entity) RETURN n LIMIT 10")
            return [{"text": record["n"]["name"]} for record in result]

    def get_data_from_neo4j(self, cypher_query):
        with self.driver.session() as session:
            result = session.run(cypher_query)
            return [record["n"] for record in result]
