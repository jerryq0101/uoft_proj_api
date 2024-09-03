# import requests

# base_url = "https://flask-heroku-test-1-19ead2b012a7.herokuapp.com/"

# # Test the helloworld resource
# response = requests.put(base_url + "helloworld/John", json={"name": "John", "money": 12, "family": 4})
# print(response.json())

# response = requests.get(base_url + "helloworld/John")
# print(response.json())

# Testing the traversal utilieis of the api
import pprint

from collections import defaultdict
import os
from dotenv import load_dotenv, dotenv_values

from traversal_util import (CourseNode, create_prerequisite_tree_from_apoc, create_full_tree_from_apoc, tree_visualization, mark_completion, course_node_to_dict, commonality_algorithm)
load_dotenv()

from neo4j import GraphDatabase

URI = os.getenv("N4J_DB_URI")
AUTH = ("neo4j", os.getenv("N4J_DB_PASS"))


def main():
    # Test the find combination function
    
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
            course_1 = "MAT309H1"
            course_2 = "MAT237Y1"
            course_3 = "MAT257Y1"

            node_1 = create_prerequisite_tree_from_apoc(session, course_1)
            node_2 = create_prerequisite_tree_from_apoc(session, course_2)
            node_3 = create_prerequisite_tree_from_apoc(session, course_3)

            print(commonality_algorithm([node_1, node_2, node_3]))

# def run_apoc_query(tx, course_code: str):
#     query = """
#     MATCH (start:Course {code: $course_code})
#     CALL apoc.path.subgraphAll(start, {
#         relationshipFilter: "Contains>",
#         labelFilter: "+Course|AND|OR"
#     })
#     YIELD nodes, relationships
#     RETURN nodes, relationships
#     """
#     result = tx.run(query, course_code=course_code)
#     return [record for record in result]

# def run_apoc_query_first_level(tx, course_code: str):
#     query = """
#     MATCH (start:Course {code: $course_code})
#     CALL apoc.path.subgraphAll(start, {
#         relationshipFilter: "Contains>",
#         labelFilter: "+Course|AND|OR"
#     })
#     YIELD nodes, relationships
#     WITH nodes, [rel IN relationships WHERE type(rel) = 'Contains' AND rel.root = $course_code] AS filtered_relationships
#     RETURN nodes, filtered_relationships AS relationships
#     """
#     result = tx.run(query, course_code=course_code)
#     return [record for record in result]



# def parse_node(node):
#     return {
#         "id": node.element_id,
#         "labels": list(node.labels),
#         "properties": dict(node)
#     }


# def parse_relationship(rel):
#     return {
#         "id": rel.element_id,
#         "type": rel.type,
#         "start_node": rel.nodes[0].element_id,
#         "end_node": rel.nodes[1].element_id,
#         "properties": dict(rel)
#     }
    

if __name__ == "__main__":
    main()