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
            
            
            # Test traversal for first level prerequisites (Where relationships are all, -[c:Contains {root: root_code}]->, root_code doens't change)
            
            # Test it out with a tree
            

            # # Create a parent node
            # parent1 = CourseNode(
            #     label="Course",
            #     code="MAT351Y1",
            #     full_name= "MAT351Y1: Partial Differential Equations",
            #     index=None
            # )
            # create_tree(
            #     parent_node=parent1,
            #     root_course_string="MAT351Y1",
            #     label="AND",
            #     code=None,
            #     full_name=None,
            #     index=181,
            #     session=session
            # )
            
            # parent2 = CourseNode(
            #     label="Course",
            #     code="CSC446H1",
            #     full_name="CSC446H1: Computational Methods for Partial Differential Equations",
            #     index=None
            # )
            # create_tree(
            #     parent_node=parent2,
            #     root_course_string="CSC446H1",
            #     label="AND",
            #     code=None,
            #     full_name=None,
            #     index=175,
            #     session=session
            # )
            # trees = {
            #     "MAT351Y1": parent1, 
            #     "CSC446H1": parent2
            # }
            # commonality = get_commonality(trees)
            # print(commonality)


            parent1 = CourseNode(
                label="Course",
                code="MAT136H1",
                full_name= "MAT136H1: Calculus II",
                index=None
            )
            create_tree(
                parent_node=parent1,
                root_course_string="MAT136H1",
                label="AND",
                code=None,
                full_name=None,
                index=5,
                session=session
            )
            dict = course_node_to_dict(parent1)
            pprint.pprint(dict)




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