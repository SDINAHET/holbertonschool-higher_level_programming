Tasks
0. Basics of HTTP/HTTPS
mandatory
Background:
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

Objective:
At the end of this exercise, students should be able to:

Differentiate between HTTP and HTTPS.
Understand the basic working and structure of HTTP requests and responses.
Recognize and explain the common HTTP methods and status codes.
Resources:
Mozilla Developer Network (MDN) - An Overview of HTTP
Difference between HTTP and HTTPS
List of HTTP status codes
Instructions:
Differentiating HTTP and HTTPS:

Read the provided resources to understand the basic differences between HTTP and HTTPS.
Jot down the main differences, focusing on security aspects.
Optional: Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request (Make sure you have the appropriate permissions).
Understanding HTTP Structure:

Visit a simple website, right-click, and choose “Inspect” or “Inspect Element”. Navigate to the “Network” tab. This shows all network requests made by the page.
Reload the page and observe the first request. Click on it. Explore the “Headers” section to understand the structure of HTTP requests and responses. You’ll see methods, paths, status codes, headers, and more.
Exploring HTTP Methods and Status Codes:

Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.
Hints:
HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content. HTTPS adds a layer of encryption, making the content unintelligible to eavesdroppers.
The “s” in “https” stands for “secure”. Websites, especially those that handle sensitive data like banking websites or email providers, typically use HTTPS.
Each HTTP status code has a specific purpose. They are grouped by their first digit: 1xx (informational), 2xx (successful), 3xx (redirection), 4xx (client errors), and 5xx (server errors).
Expected Output:
A brief summary explaining the differences between HTTP and HTTPS.
A depiction or outline of the structure of an HTTP request and response.
Lists of common HTTP methods and status codes with their descriptions and possible use cases. For example:
Method: GET, Description: Retrieves data, Use case: Fetching a web page or data from an API.
Status Code: 404, Description: Not Found, Scenario: When a requested page or resource isn’t available on the server.
0/0 pts
1. Consume data from an API using command line tools (curl)
mandatory
Background:
curl (Client URL) is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more). It’s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering curl, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

Objective:
At the end of this exercise, students should be able to:

Install and use curl from the command line.
Construct and execute basic API requests using curl, including setting headers and inspecting the output.
Interpret the results of common API requests.
Resources:
curl - Everything curl
Using cURL to interact with HTTP APIs
Public API to play with: JSONPlaceholder
Instructions:
Installing and Basic Interaction with curl:

Install curl on your system. It’s usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of curl.
Once installed, run curl --version to confirm its availability.
Use curl to fetch the content of a webpage. For instance: curl http://example.com.
Fetching Data from an API:

Use curl to retrieve posts from JSONPlaceholder: curl https://jsonplaceholder.typicode.com/posts
Observe the output. It should be a JSON array of posts.
Using Headers and Other Options with curl:

Fetch only the headers of the same request using curl -I https://jsonplaceholder.typicode.com/posts.
Use curl to make a POST request to the same API: curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
Hints:
The -I flag in curl fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
With the -X flag, you can specify an HTTP method for your request. For example, -X POST will make a POST request.
The -d flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like jq for JSON formatting and highlighting.
Expected Output:
Upon running curl --version, you should see details about your installed version of curl, including supported protocols.
Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like userId, id, title, and body.
Fetching only headers should give a concise output showing status codes and headers without the actual content.
Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an id of 101 (since it doesn’t actually save the new post, but simulates the creation).
0/0 pts
2. Consuming and processing data from an API using Python
mandatory
Background:
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The requests library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

Objective:
At the end of this exercise, students should be able to:

Utilize the requests library to send HTTP requests and process responses.
Parse and manipulate JSON data using Python.
Convert structured data into other formats, e.g., CSV.
Resources:
Python Requests Library
Working with JSON data in Python
Public API to experiment with: JSONPlaceholder
Instructions:
If not installed, install the requests library using pip: pip install requests.

Write a basic Python script to fetch posts from JSONPlaceholder using requests.get().

Create a function fetch_and_print_posts() that fetches all post from JSONPlaceholder.

Print the status code of the response i.e. Status Code: 200
If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
Iterate through the parsed JSON data and print out the titles of all the posts.
Create a function fetch_and_save_posts() that fetches all post from JSONPlaceholder.

If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
Using Python’s csv module, write this data into a CSV file called posts.csv with columns corresponding to the dictionary keys.
$ cat main_02_requests.py
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()

$ python3 main_02_requests.py
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
dolorem eum magni eos aperiam quia
...
Hints:
The requests.get() function returns a Response object, from which you can access various properties like status_code, headers, and methods like json().
When converting the parsed JSON data into a list of dictionaries, you might find list comprehensions useful for concise code.
The csv.DictWriter class can be a convenient way to write dictionaries to a CSV file, as it automatically handles headers based on dictionary keys.
Expected Output:
After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
When parsing JSON data, you should see printed titles of the posts, e.g., “sunt aut facere repellat provident occaecati excepturi optio reprehenderit.”
After the data manipulation and conversion task, you should have a CSV file with columns id, title, and body. Each row in the CSV should correspond to a post from the fetched data.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
File: task_02_requests.py
0/3 pts
3. Develop a simple API using Python with the `http.server` module
mandatory
Background:
The http.server module in Python’s standard library provides basic classes for implementing web servers. While it’s not typically used for production applications, it’s a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.

Objective:
At the end of this exercise, students should be able to:

Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
Resources:
Python docs: http.server — HTTP servers
A simple example of using Python’s http.server
Instructions:
Setting Up a Basic HTTP Server:

Use the http.server module to set up a simple HTTP server. Start by creating a subclass of http.server.BaseHTTPRequestHandler.
Implement the do_GET method to handle GET requests. Within this method, send a simple text response back to the client: “Hello, this is a simple API!”.
Start the server on a specific port (8000) and test it by visiting http://localhost:8000 in your browser or using curl.
Serving JSON Data:

Modify the do_GET method in your server class to serve a sample JSON data when the endpoint /data is accessed.
You should return a simple dataset: {"name": "John", "age": 30, "city": "New York"}.
Ensure that the correct content type (application/json) header is set in the response.
Handling Different Endpoints:

Add an /status endpoint to check the API status. It shoud return OK.
Implement error handling. If the user tries to access an undefined endpoint, return a 404 Not Found status with an appropriate message.
Hints:
When sending headers using http.server, the send_response method is handy. You can also use send_header to specify specific headers, and don’t forget to end headers with end_headers.
For serving JSON data, you’ll want to convert a Python dictionary to a JSON string. The json module in Python’s standard library will be beneficial.
When checking the path of the request, the path attribute of the request handler (self.path) can be used to route requests to different endpoints.
Expected Output:
On visiting http://localhost:8000, you should see the text: “Hello, this is a simple API!”.
On accessing the endpoint /data, a JSON response with the sample dataset should be returned: {"name": "John", "age": 30, "city": "New York"}.
When visiting /info, you might see something like: {"version": "1.0", "description": "A simple API built with http.server"}.
Accessing any other undefined endpoint should return a 404 Not Found status with a message like “Endpoint not found”.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
File: task_03_http_server.py
0/4 pts
4. Develop a Simple API using Python with Flask
mandatory
Background:
Flask is a lightweight web framework for Python, which is especially popular for creating small to medium web applications and RESTful APIs. Its minimalist and modular approach makes it a great choice for beginners to delve into web development without the overhead of more complex frameworks.

Objective:
At the end of this exercise, students should be able to: 1. Set up a Flask application and run a development server. 2. Define and handle routes with Flask to respond to different endpoints. 3. Serve JSON data using Flask. 4. Understand the basics of request handling and response formation in Flask. 5. Handle POST requests to add new data to the API.

Resources:
Flask Official Documentation Start with the Quickstart section: “A Minimal Application” to get an overall idea on how the framework works.
Instructions:
Setting Up Flask:

Install Flask using pip: pip install Flask.
Create a new Python file and import Flask: from flask import Flask.
Instantiate a Flask web server from the Flask module: app = Flask(__name__).
Creating Your First Endpoint:

Define a route for the root URL (“/”) and create a function (def home():) to handle this route. Within the function, return a string: “Welcome to the Flask API!”.
Run the Flask development server with: if __name__ == "__main__": app.run().
Visit http://localhost:5000 in your browser or use curl to see the message.
Serving JSON Data:

Import the jsonify function from Flask: from flask import jsonify.
Create a new route /data and associate a function with it. Inside this function, return a JSON response using jsonify(). This should return a list of all the usernames stored in the API.
Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
Example dictionary: users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
Expanding Your API:

Add a few more endpoints to simulate different functionalities:
/status: It should return OK.
/users/<username>: Returns the full object corresponding to the provided username. (Hint: Use Flask’s dynamic route feature)
Handling POST Requests:

Import the request object from Flask: from flask import request.
Create a new route /add_user that accepts POST requests.
This route should:
Parse the incoming JSON data. Example data: {"username": "john", "name": "John", "age": 30, "city": "New York"}
Add the new user to the users dictionary using username as the key.
Return a confirmation message with the added user’s data.
Test your code:
Test your application using the flask CLI to run the development server.

$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Use curl or a python script to test your API.

Hints:
Flask routes are defined using the @app.route() decorator, followed by a function that returns the desired response for that route.
For serving dynamic content in routes, Flask allows you to add variables to the route (e.g., <variable_name>). These can be captured in your function parameters.
The jsonify() function in Flask turns a Python dictionary or list into a response with application/json content-type.
Flask’s development server reloads automatically on code changes. However, for certain types of changes (like adding new files), you might need to restart the server.
Here’s the rewritten section to match the new requirements:

Expected Output:
Accessing http://localhost:5000 should show the message: "Welcome to the Flask API!".
Visiting http://localhost:5000/data should return a JSON response with a list of all usernames stored in the API. For example, if the users dictionary contains {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}, the response should be:
["jane", "john"]
The /status endpoint should return the string: "OK".
Accessing /users/jane should return the full object corresponding to the username “jane”. For example:
{
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
}
Similarly, accessing /users/john should return:
{
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
}
But if it doesn’t exist, return {"error": "User not found"}

Posting a new user to /add_user should add the user to the users dictionary and return a confirmation message with the user’s data. For example, posting:
{
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}
should return:

{
        "message": "User added",
        "user": {
                "username": "alice",
                "name": "Alice",
                "age": 25,
                "city": "San Francisco"
        }
}
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
File: task_04_flask.py
0/5 pts
5. API Security and Authentication Techniques
mandatory
Background:
API security is of paramount importance, especially when the API is exposed to the wider internet. There are many risks, including unauthorized data access, data tampering, and denial-of-service attacks. One fundamental method of securing APIs is to use authentication and authorization mechanisms, ensuring only authorized users can access certain resources.

Objective:
At the end of this exercise, students should be able to:

Understand the importance of API security.
Implement basic authentication using Flask.
Set up token-based authentication with JSON Web Tokens (JWT).
Differentiate between authentication and authorization.
Resources:
Flask-HTTPAuth
Flask-JWT-Extended
Introduction to JSON Web Tokens
Instructions:
Basic Authentication:
Install Flask-HTTPAuth:

Run: pip install Flask-HTTPAuth.
Set up Basic HTTP Authentication:

Create a list of users and their hashed passwords.
Use the werkzeug.security library for password hashing and verification.
Protect Routes with Basic Authentication:

Use the @auth.login_required decorator to protect certain routes.
Token-based Authentication with JWT:
Install Flask-JWT-Extended:

Run: pip install Flask-JWT-Extended.
Set up JWT-based Authentication:

Use a secret key for token generation and validation.
Create a route /login where users can log in with their credentials and receive a JWT token.
Protect Routes with JWT Tokens:

Use the @jwt_required() decorator to protect certain routes.
Implement Role-based Access Control:

Add roles (e.g., admin, user) to your users.
Create routes that should only be accessible to certain roles.
Implement checks to ensure the user’s role matches the required role for accessing specific routes.
Hints:
For basic authentication, store passwords securely using werkzeug.security.generate_password_hash and verify them using werkzeug.security.check_password_hash.
Embed user information, such as roles, within the JWT token payload.
Use a strong secret key for JWT token generation and validation.
Utilize get_jwt_identity() to retrieve user information from the current JWT token.
API Specifications:
User Data:
Users should be stored in memory using a dictionary with the following structure:
  users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
  }
Endpoints:
Basic Authentication:
Protected Route:
URL: /basic-protected
Method: GET
Description: Returns a message "Basic Auth: Access Granted" if the user provides valid basic authentication credentials.
Authentication: Basic
JWT Authentication:
Login:

URL: /login
Method: POST
Description: Accepts JSON payload with username and password. Returns a JWT token if credentials are valid.
Example Request:
   {
       "username": "user1",
       "password": "password"
   }
Example Response:
   {
       "access_token": "<JWT_TOKEN>"
   }
JWT Protected Route:

URL: /jwt-protected
Method: GET
Description: Returns a message "JWT Auth: Access Granted" if the user provides a valid JWT token.
Authentication: JWT
Role-based Protected Route:

URL: /admin-only
Method: GET
Description: Returns a message "Admin Access: Granted" if the user is an admin.
Authentication: JWT with role check
Expected Output:
Accessing /basic-protected without credentials should return a 401 Unauthorized response.
Accessing /basic-protected with valid credentials should return "Basic Auth: Access Granted".
Posting valid credentials to /login should return a JWT token.
Accessing /jwt-protected without a token or with an invalid token should return a 401 Unauthorized response.
Accessing /jwt-protected with a valid token should return "JWT Auth: Access Granted".
Accessing /admin-only with a non-admin token should return a 403 Forbidden response.
Accessing /admin-only with an admin token should return "Admin Access: Granted".
Important Note:
When implementing authentication in your Flask API, ensure that all authentication errors return a 401 Unauthorized response. This includes errors due to missing, invalid, expired, or malformed tokens. Returning a consistent 401 status code for authentication errors is crucial for passing the automated tests. Failure to return a 401 status code for these errors may result in failing tests.

Hints:
Custom Error Handlers: Use Flask-JWT-Extended‘s decorators to create custom error handlers for different types of JWT errors.
Here are some examples:

  from flask_jwt_extended import JWTManager

  app = Flask(__name__)
  jwt = JWTManager(app)

  @jwt.unauthorized_loader
  def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

  @jwt.invalid_token_loader
  def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

  @jwt.expired_token_loader
  def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

  @jwt.revoked_token_loader
  def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

  @jwt.needs_fresh_token_loader
  def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
File: task_05_basic_security.py
0/11 pts
