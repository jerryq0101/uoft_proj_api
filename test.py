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

from traversal_util import (CourseNode, create_tree, tree_visualization, mark_completion)
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
            # parent = CourseNode(
            #     label="Course",
            #     code="MAT334H1",
            #     full_name="MAT334H1: Complex Variables",
            #     index=None
            # )
            # create_tree(
            #     parent_node=parent,
            #     root_course_string="MAT334H1",
            #     label="AND",
            #     code=None,
            #     full_name=None,
            #     index=184,
            #     session=session
            # )
            
            # tree_visualization(parent)
            
            test_mark_completion()


def test_mark_completion():
    # Create the sample tree structure
    root = CourseNode(label="Course", code="MAT334H1", full_name="Complex Variables")
    and_node = CourseNode(label="AND", index=1)
    root.add_child(and_node)

    or_node1 = CourseNode(label="OR", index=2)
    or_node2 = CourseNode(label="OR", index=3)
    and_node.add_child(or_node1)
    and_node.add_child(or_node2)

    or_node1.add_child(CourseNode(label="Course", code="MAT223H1", full_name="Linear Algebra I"))
    or_node1.add_child(CourseNode(label="Course", code="MAT240H1", full_name="Algebra I"))

    or_node2.add_child(CourseNode(label="Course", code="MAT235Y1", full_name="Calculus II"))
    or_node2.add_child(CourseNode(label="Course", code="MAT237Y1", full_name="Multivariable Calculus"))
    or_node2.add_child(CourseNode(label="Course", code="MAT257Y1", full_name="Analysis II"))

    # Test case 1: No courses completed
    mark_completion(root, [])
    print("Root Marked:", root.marked)
    print("And1 Marked:", and_node.marked)
    print("Or1 Marked:", or_node1.marked)
    print("Or2 Marked:", or_node2.marked)
    assert not root.marked
    assert not and_node.marked
    assert not or_node1.marked
    assert not or_node2.marked

    
    # Test case 2: One course from each OR node completed
    mark_completion(root, ["MAT223H1", "MAT235Y1"])
    print("Root Marked:", root.marked)
    print("And1 Marked:", and_node.marked)
    print("Or1 Marked:", or_node1.marked)
    print("Or2 Marked:", or_node2.marked)
    
    assert root.marked
    assert and_node.marked
    assert or_node1.marked
    assert or_node2.marked

    # Test case 3: All courses completed
    mark_completion(root, ["MAT223H1", "MAT240H1", "MAT235Y1", "MAT237Y1", "MAT257Y1"])
    assert root.marked
    assert and_node.marked
    assert or_node1.marked
    assert or_node2.marked

    # Test case 4: Only one OR node satisfied
    mark_completion(root, ["MAT223H1"])
    assert not root.marked
    assert not and_node.marked
    assert or_node1.marked
    assert not or_node2.marked

    print("All test cases passed!")


    
    # traversal.get_first_level_children(driver) 
    

if __name__ == "__main__":
    main()