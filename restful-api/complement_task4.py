@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

@app.route('/add_user', methods=['POST']) # 5.Handling POST Requests/Create a new route /add_user that accepts POST requests.
def add_user():
    user_data = request.get_json()

    # Validate the incoming data
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Check if the user already exists
    username = user_data['username']

    # Check if the user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    # Return a success message
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/holbertonschool-high
er_level_programming/restful-api# ./task_04_flask.py
 * Serving Flask app 'task_04_flask'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Oct/2024 11:24:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 11:25:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 11:25:25] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 11:25:43] "GET /user/jane HTTP/1.1" 404 -
127.0.0.1 - - [11/Oct/2024 11:26:34] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 11:28:43] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 11:29:02] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 11:29:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 11:29:29] "GET /add_user HTTP/1.1" 405 -
^Croot@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/holbert
onschool-higher_level_programming/restful-api# ./task_04_flask.py
 * Serving Flask app 'task_04_flask'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Oct/2024 12:33:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 12:33:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 12:33:52] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Oct/2024 12:34:09] "GET /user/jane HTTP/1.1" 404 -
127.0.0.1 - - [11/Oct/2024 12:34:15] "GET /user HTTP/1.1" 404 -
127.0.0.1 - - [11/Oct/2024 12:34:23] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 12:34:33] "GET /add_user HTTP/1.1" 405 -
curl -X POST http://localhost:5000/add_user \
-H "Content-Type: application/json" \
-d '{"name": "Jane", "email": "jane.doe@example.com"}'
127.0.0.1 - - [11/Oct/2024 12:37:18] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 12:37:20] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 12:37:47] "GET /users/jane HTTP/1.1" 404 -
127.0.0.1 - - [11/Oct/2024 12:43:26] "GET /add_user HTTP/1.1" 405 -
127.0.0.1 - - [11/Oct/2024 12:43:31] "GET /add_user HTTP/1.1" 405 -
