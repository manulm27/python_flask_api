from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "done": True, "label": "Sample Todo 1" }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    users = jsonify(todos)
    return users

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)