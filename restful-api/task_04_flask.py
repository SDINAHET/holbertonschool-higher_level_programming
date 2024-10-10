#!/usr/bin/python3

from flask import Flask # 1.Setting Up Flask / Create a new Python file and import Flask
from flask import jsonify # 3.Serving JSON Data / Import the jsonify function from Flask
from flask import request # 5.Handling POST Requests/Import the request object

app = Flask(__name__) # Instantiate a Flask web server from the Flask module

PORT = 5000 # 2.Creating Your First Endpoint / Visit http://localhost:5000 in your browser or use curl to see the message.

# In-memory storage for users / dictionary / This should return a list of all the usernames stored in the API.
# 3.Serving JSON Data / Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
# 5.Handling POST Requests/ Parse the incoming JSON data.
# users = {

# }
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

@app.route('/add_user', methods=['POST']) # 5.Handling POST Requests/Create a new route /add_user that accepts POST requests.
def add_user():
    data = request.get_json()

    # Validate the incoming data
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add user to the dictionary  5.Handling POST Requests/Parse the incoming JSON
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return jsonify({ # Add the new user to the users dictionary using username as the key
        "message": "User added",
        "user": users[username]
    }), 201 # 5.Handling POST Requests/ Return a confirmation message with the added user’s data.

# Dynamic route example
@app.route("/user/<username>")
def show_user_profile(username):
    # A dictionary response using the dynamic content captured in the route
    return jsonify({"username": username, "message": f"Hello, {username}!"})

# Another dynamic route with an integer
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return jsonify({"post_id": post_id, "content": f"This is the content of post {post_id}."})

if __name__ == "__main__": # 2.Creating Your First Endpoint / Run the Flask development server
    app.run(port=5000, debug=False)
