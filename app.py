from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
import json

app = Flask(__name__)
api = Api(app)

data = { "students": [
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
}

parser = reqparse.RequestParser()
parser.add_argument('task')

class StudentList(Resource):
    def get(self):
        print('debug: sending full list')
        return data
    
    def post(self):
        data['student'].append(request.data)
        return data, 201

api.add_resource(StudentList, '/students')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)