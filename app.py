from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
import json

app = Flask(__name__)
api = Api(app)

data = [
     {
        "Emanuel": {
            "hostname": "3.123.123.123"
        }
        },
    {
        "Emanuelina": {
            "hostname": "231.213.123.23"
        }
    }
] 

class StudentList(Resource):
    def get(self):
        print('debug: sending full list')
        return data
    
    def post(self):
        new_student = json.loads(request.data)
        print(new_student)
        data.append(new_student)
        return data, 201

api.add_resource(StudentList, '/students')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)