from flask import Flask
from flask_restful import Api, Resource
import subprocess

app = Flask(__name__)
api = Api(app)

class Ping(Resource):
    def get(self, ip):
        try:
            process = subprocess.Popen(["ping", ip, "-c", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            exit_code = process.returncode

            if exit_code == 0:
                response_message = f"Ping to {ip} was successful:\n{stdout}"
            else:
                response_message = f"Ping to {ip} failed:\n{stderr}"

            # Split the lines and convert them into a list
            response_lines = response_message.splitlines()

            return {"message": response_lines}
        except Exception as e:
            return {"error": str(e)}

api.add_resource(Ping, '/ping/<string:ip>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)