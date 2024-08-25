from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
from neo4j_conn import Neo4jConn

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
            full_name = result.records[0]["full_name"]
            print(full_name)
            print(result)
            
            return {
                "code": course_name,
                "full_name": full_name
            }
    

api.add_resource(Helloworld, "/helloworld/<string:name>")
api.add_resource(CourseQuery, "/course/<string:course_name>")

if __name__ == "__main__":
    app.run()