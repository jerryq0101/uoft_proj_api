import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from neo4j import GraphDatabase

URI = os.getenv("N4J_DB_URI")
AUTH = ("neo4j", os.getenv("N4J_DB_PASS"))


class Neo4jConn:
    """
    A class for creating the connection instance to the Neo4j database used in the Flask API

    Attributes:
    - _driver (GraphDatabase.driver): The Neo4j driver instance

    """
    def __init__(self):
        """
        Initialize the Neo4j connection instance
        
        Raises:
        - Exception: If the connection to the database fails
        """
        self._driver = GraphDatabase.driver(URI, auth=AUTH)
        self._driver.verify_connectivity()
    
    def close(self):
        """
        Close the Neo4j connection instance. Generally never used, as the api should be hosted ongoing.
        """
        self._driver.close()