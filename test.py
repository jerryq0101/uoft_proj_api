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

from traversal_util import (CourseNode, create_tree, tree_visualization, mark_completion, course_node_to_dict)
load_dotenv()

from neo4j import GraphDatabase

URI = os.getenv("N4J_DB_URI")
AUTH = ("neo4j", os.getenv("N4J_DB_PASS"))


def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
            
            dict_course = {}
            dict_AND = {}
            dict_OR = {}

            dict_neo4j_all = {}

            # Test apoc functions 
            course_I_want = "MAT257Y1"
            result = session.execute_read(run_apoc_query, course_I_want)

            for record in result:
                nodes = record["nodes"]
                relationships = record["relationships"]

                parsed_nodes = [parse_node(node) for node in nodes]
                parsed_relationships = [parse_relationship(rel) for rel in relationships]
                
                
                print("Nodes:")
                for node in parsed_nodes:
                    print(f"  ID: {node['id']}")
                    print(f"  Labels: {', '.join(node['labels'])}")
                    print(f"  Properties: {node['properties']}")
                    print()

                    # Operations
                    neo4j_id = node["id"]
                    node_label = node["labels"][0]
                    node_properties = node["properties"]
                    
                    if node_label == "Course":
                        code = node_properties["code"]
                        full_name = node_properties["full_name"]
                        course_node = CourseNode(
                            label="Course",
                            code=code,
                            full_name=full_name,
                            index=None
                        )
                        dict_course[code] = course_node
                        dict_neo4j_all[neo4j_id] = course_node
                    elif node_label == "AND":
                        index = node_properties["index"]
                        and_node = CourseNode(
                            label="AND",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_AND[index] = and_node
                        dict_neo4j_all[neo4j_id] = and_node
                    elif node_label == "OR":
                        index = node_properties["index"]
                        or_node = CourseNode(
                            label="OR",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_OR[index] = or_node
                        dict_neo4j_all[neo4j_id] = or_node

                print("Relationships:")
                for rel in parsed_relationships:
                    print(f"  ID: {rel['id']}")
                    print(f"  Type: {rel['type']}")
                    print(f"  Start Node: {rel['start_node']}")
                    print(f"  End Node: {rel['end_node']}")
                    print(f"  Properties: {rel['properties']}")
                    print()

                    # Operations
                    start_node_neo4j_id = rel["start_node"]
                    end_node_neo4j_id = rel["end_node"]

                    start_node_obj = dict_neo4j_all[start_node_neo4j_id]
                    end_node_obj = dict_neo4j_all[end_node_neo4j_id]

                    start_node_obj.add_child(end_node_obj)

            print("Tree:")
            tree_visualization(dict_course[course_I_want])


def run_apoc_query(tx, course_code: str):
    query = """
    MATCH (start:Course {code: $course_code})
    CALL apoc.path.subgraphAll(start, {
        relationshipFilter: "Contains>",
        labelFilter: "+Course|AND|OR"
    })
    YIELD nodes, relationships
    RETURN nodes, relationships
    """
    result = tx.run(query, course_code=course_code)
    return [record for record in result]

def run_apoc_query_first_level(tx, course_code: str):
    query = """
    MATCH (start:Course {code: $course_code})
    CALL apoc.path.subgraphAll(start, {
        relationshipFilter: "Contains>",
        labelFilter: "+Course|AND|OR"
    })
    YIELD nodes, relationships
    WITH nodes, [rel IN relationships WHERE type(rel) = 'Contains' AND rel.root = $course_code] AS filtered_relationships
    RETURN nodes, filtered_relationships AS relationships
    """
    result = tx.run(query, course_code=course_code)
    return [record for record in result]



def parse_node(node):
    return {
        "id": node.element_id,
        "labels": list(node.labels),
        "properties": dict(node)
    }


def parse_relationship(rel):
    return {
        "id": rel.element_id,
        "type": rel.type,
        "start_node": rel.nodes[0].element_id,
        "end_node": rel.nodes[1].element_id,
        "properties": dict(rel)
    }
    

if __name__ == "__main__":
    main()