# import requests

# base_url = "https://flask-heroku-test-1-19ead2b012a7.herokuapp.com/"

# # Test the helloworld resource
# response = requests.put(base_url + "helloworld/John", json={"name": "John", "money": 12, "family": 4})
# print(response.json())

# response = requests.get(base_url + "helloworld/John")
# print(response.json())

# Testing the traversal utilieis of the api

import os
from dotenv import load_dotenv, dotenv_values

from traversal_util import (CourseNode, create_tree, tree_visualization)
load_dotenv()

from neo4j import GraphDatabase

URI = os.getenv("N4J_DB_URI")
AUTH = ("neo4j", os.getenv("N4J_DB_PASS"))


def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
            
            # if I call function through an class object it fucks up, 
            # Is a class even necessary? 
            # change the class to a purely utility based class

            # session.execute_read(
            #     TraversalUtilities.find_course_children, 
            #     "MAT354H1",
            #     "",
            #     "MAT354H1"
            # )

            # print(session.execute_read(
            #     TraversalUtilities.find_or_children,
            #     "OR",
            #     26,
            #     "STA302H1"
            # ))
            
            # Test traversal for first level prerequisites (Where relationships are all, -[c:Contains {root: root_code}]->, root_code doens't change)
            
            # Create a parent node
            parent = CourseNode(
                label="Course",
                code="MAT334H1",
                full_name="MAT334H1: Complex Variables",
                index=None
            )
            create_tree(
                parent_node=parent,
                root_course_string="MAT334H1",
                label="AND",
                code=None,
                full_name=None,
                index=184,
                session=session
            )
            
            tree_visualization(parent)



    
    # traversal.get_first_level_children(driver) 
    

if __name__ == "__main__":
    main()