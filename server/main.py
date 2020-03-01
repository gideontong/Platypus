from flask import Flask, jsonify, make_response
import json
import re
import werkzeug.datastructures

app = Flask(__name__)

@app.route('/<string:package>/<string:version>', methods = ['GET'])
def get(package, version):
    package = package.lower()
    version = re.search('[0-9]*\.[0-9]*', version).group()
    try:
        if "apache" in package or "httpd" in package:
            package = "httpd"
        elif "nginx" in package:
            package = "nginx"
        elif "wordpress" in package:
            package = "wp"
        elif "postgres" in package:
            package = "postgresql"
        with open('target_' + package + '_cve.json') as file:
            data = json.load(file)
            return make_response(jsonify(data[version]), 200)
    except:
        return make_response(jsonify({"failure": "failure"}), 500)

def http(request):
    with app.app_context():
        headers = werkzeug.datastructures.Headers()
        for key, value in request.headers.items():
            headers.add(key, value)
        with app.test_request_context(method=request.method, base_url=request.base_url, path=request.path, query_string=request.query_string, headers=headers, data=request.form):
            try:
                rv = app.preprocess_request()
                if rv is None:
                    rv = app.dispatch_request()
            except Exception as e:
                rv = app.handle_user_exception(e)
            response = app.make_response(rv)
            return app.process_response(response)
