import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from neo4j import GraphDatabase

URI = os.getenv("N4J_DB_URI")
AUTH = ("neo4j", os.getenv("N4J_DB_PASS"))

class Neo4jConn:
    def __init__(self):
        self._driver = GraphDatabase.driver(URI, auth=AUTH)
        self._driver.verify_connectivity()
    
    
    def close(self):
        self._driver.close()

        
