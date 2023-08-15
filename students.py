from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

myName = "Emanuel"
myIP = '<Public-IP>'
myFriend = '<IP>:<PORT>'

class StudentList(Resource):
    def get(self):
        print('debug: sending full list')
        return "OK"
    
    def post(self):
        return "Ok"

api.add_resource(StudentList, '/students')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)