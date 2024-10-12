#!/usr/bin/python3

from flask import Flask # 1.Setting Up Flask / Create a new Python file and import Flask
from flask import jsonify # 3.Serving JSON Data / Import the jsonify function from Flask
from flask import request # 5.Handling POST Requests/Import the request object

app = Flask(__name__) # Instantiate a Flask web server from the Flask module

PORT = 5000 # 2.Creating Your First Endpoint / Visit http://localhost:5000 in your browser or use curl to see the message.

# In-memory storage for users / dictionary / This should return a list of all the usernames stored in the API.
# 3.Serving JSON Data / Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
# 5.Handling POST Requests/ Parse the incoming JSON data.
users = {}
# users = {
#    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
#    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
# }

@app.route("/") # decorator, followed by a function that returns the desired response for that route.
def home(): # 2.Creating Your First Endpoint / Define a route for the root URL (“/”) and create a function
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET']) # 3.Serving JSON Data / Create a new route /data and associate a function with it
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET']) # 4.Expanding Your API / Add a few more endpoint /status: It should return OK.
def status():
    return "OK"

@app.route('/users/<username>', methods=['GET']) # 4.Expanding Your API / Add a few more endpoint //users/<username>: Returns the full object corresponding to the provided username. (Hint: Use Flask’s dynamic route feature)
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__": # 2.Creating Your First Endpoint / Run the Flask development server
    app.run(port=5000, debug=False)
