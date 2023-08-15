from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

TODOS = { 'todo1': {'task': 'Build an API'},
    'todo2': {'task': '???'}
}
parser = reqparse.RequestParser()
parser.add_argument('task')

class TodoList(Resource):
    def get(self):
        print('debug: sending full list')
        return TODOS
    
    def post(self):
        args= parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = f'todo{todo_id}'
        TODOS[todo_id] = {'task': args['task']}
        print(f'debug: added {todo_id}')
        return TODOS[todo_id], 201
    
class Todo(Resource):
    def get (self, todo_id):
        print(f'debug: sending {todo_id}')
        return TODOS[todo_id]
    def abort_if_todo_doesnt_exist(self, todo_id):
        if todo_id not in TODOS:
            abort(404, message=f'Todo {todo_id} doesn\'t exist')
    def put(self, todo_id):
        print(f'debug: updating {todo_id}')
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    def delete(self, todo_id):
        print(f'debug: deleting {todo_id}')
        self.abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
class Ping(Resource):
    def get(self, ip):
        res = get()

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Ping, '/ping/<ip>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)