from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("name", type=str, help="Name of the person")
person_put_args.add_argument("money", type=int, help="Money of the person")
person_put_args.add_argument("family", type=int, help="Family member amount of the person")

people = {}

class Helloworld(Resource):
    # result is initially returned as an SQLalchemy instance, define the information of the fields in the instance, and the marshal_with serializes (converts) it into json format
    # Put it above any method that you want to have the return serialized
    def get(self, name):
        if name not in people:
            abort(404, description="Person not found")
        return people[name]

    def put(self, name):
        args = person_put_args.parse_args()
        people[name] = args
        return people[name], 201

api.add_resource(Helloworld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run()