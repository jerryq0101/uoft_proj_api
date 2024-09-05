# This file is used to test out algorithms and database connections.

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

    

if __name__ == "__main__":
    main()