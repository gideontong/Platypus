from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class Stuff(Resource):
    def get(self, package, version):
        try:
            with open('target_' + package + '_cve.json') as file:
                data = json.load(file)
                return data[version], 200
        except:
            return "Failure", 500

api.add_resource(Stuff, "/<string:package>/<string:version>")

app.run(debug=True)