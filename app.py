from flask import Flask, request, abort, jsonify
from flask_restful import Api, Resource, reqparse
from neo4j_conn import Neo4jConn
from traversal_util import CourseNode, create_full_tree_from_apoc, create_prerequisite_tree_from_apoc, mark_completion, course_node_to_dict, commonality_algorithm

app = Flask(__name__)
api = Api(app)

# Initialize neo4j connection
neo4j = Neo4jConn()

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("name", type=str, help="Name of the person")
person_put_args.add_argument("money", type=int, help="Money of the person")
person_put_args.add_argument("family", type=int, help="Family member amount of the person")

people = {}

class Helloworld(Resource):
    def get(self, name):
        if name not in people:
            abort(404, description="Person not found")
        return people[name]

    def put(self, name):
        args = person_put_args.parse_args()
        people[name] = args
        return people[name], 201

tree = {}

class CourseQuery(Resource):
    @app.route("/course/<string:course_name>")
    def get(self, course_name):
        """
        Gets the course details and the full name of the course itself
        """
        print("This request works")
        # Check # of courses that match with course_name
        result = neo4j._driver.execute_query(
            """
            MATCH (c:Course {code: $code})
            RETURN count(c) as count
            """,
            code=course_name
        )
        neo4j.close()
        print("RESULT", result)
        count = result.records[0]["count"]
        if count == 0:
            abort(404, description="Course not found")
        else:
            # Get the full name of the course
            result = neo4j._driver.execute_query(
                """
                MATCH (c:Course {code: $code})
                RETURN c.full_name as full_name
                """,
                code=course_name
            )
            neo4j.close()
            full_name = result.records[0]["full_name"]
            print(full_name)
            print(result)
            
            return {
                "code": course_name,
                "full_name": full_name
            }


    @app.route("/course/")
    def post(self):

        data = request.json
        if not data:
            abort(400, description="Invalid JSON or no data provided")
        
        completed_courses = data.get("completed_courses", [])
        desired_courses = data.get("desired_courses", [])
        tree_choice = data.get("tree_choice", "full")

        arr_of_dicts = []
        
        arr_tree_nodes = []

        with neo4j._driver.session() as session:
            for course in desired_courses:
                if tree_choice == "full":
                    tree = create_full_tree_from_apoc(session, course)
                    arr_tree_nodes.append(tree)
                    mark_completion(tree, completed_courses)
                    dict_of_node = course_node_to_dict(tree)
                    arr_of_dicts.append(dict_of_node)
                else:
                    tree = create_prerequisite_tree_from_apoc(session, course)
                    arr_tree_nodes.append(tree)
                    mark_completion(tree, completed_courses)
                    dict_of_node = course_node_to_dict(tree)
                    arr_of_dicts.append(dict_of_node)
        
        commonality_dict = commonality_algorithm(arr_tree_nodes)
        
        return {
            "course_trees": arr_of_dicts,
            "commonality": commonality_dict
        }, 200
    

api.add_resource(Helloworld, "/helloworld/<string:name>")
api.add_resource(CourseQuery, "/course/", "/course/<string:course_name>")


if __name__ == "__main__":
    app.run()