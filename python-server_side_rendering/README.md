Python-server_side_rendering

## Task0:
To create this templating program, let's break down the requirements step-by-step. We will use Python's string manipulation and file handling capabilities to read a template, process data for multiple attendees, and output personalized invitation files. Here’s how we can implement each part of this task:

Steps to Implement generate_invitations
Validate Input Types and Content: Ensure template is a string and attendees is a list of dictionaries. If either is incorrect, log an error message and exit.
Handle Empty Inputs: Check if template or attendees list is empty. Log a message and exit if so.
Process Each Attendee: Loop over each dictionary in attendees, and use placeholders to substitute values from the dictionary, using "N/A" if a value is missing.
Write Output Files: Create output files in a sequence (e.g., output_1.txt, output_2.txt, etc.) for each processed invitation.
Code Implementation
Here's the complete Python code for the generate_invitations function:

python
Copier le code
import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Create the personalized invitation text by replacing placeholders
        invitation_text = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Replace each placeholder with actual value or "N/A" if missing
            value = attendee.get(key, "N/A") or "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", value)

        # Write the personalized invitation to a file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation_text)
            print(f"Invitation file created: {output_filename}")
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")
Explanation of Key Sections
Input Validation: We check if template is a string and attendees is a list of dictionaries. If not, an error message is printed and the function exits.
Empty Template and Attendees Check: If the template or attendees are empty, it logs a message and stops the function.
Generating Invitations: For each attendee, we replace placeholders ({name}, {event_title}, {event_date}, and {event_location}) in the template. If any key is missing, it substitutes "N/A".
Writing Files: Each processed template is written to a file named output_X.txt, where X is the index of the attendee in the list.
Example Template File: template.txt
Save this content in a file named template.txt:

plaintext
Copier le code
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
Example Data and Main File for Testing
Save the following code in your main file (for example, main.py) to test the program:

python
Copier le code
from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
Testing the Program
Run main.py in your Python environment.
This should read template.txt, process the attendees list, and generate files named output_1.txt, output_2.txt, etc.
Each output file should contain a personalized invitation, with missing data fields replaced by "N/A".
Expected Output in Files
output_1.txt for Alice:

plaintext
Copier le code
Hello Alice,

You are invited to the Python Conference on 2023-07-15 at New York.

We look forward to your presence.

Best regards,
Event Team
output_2.txt for Bob:

plaintext
Copier le code
Hello Bob,

You are invited to the Data Science Workshop on 2023-08-20 at San Francisco.

We look forward to your presence.

Best regards,
Event Team
output_3.txt for Charlie (missing event_date):

plaintext
Copier le code
Hello Charlie,

You are invited to the AI Summit on N/A at Boston.

We look forward to your presence.

Best regards,
Event Team
Notes
Ensure template.txt exists in the same directory or update the path as needed.
Modify the file paths and names as per your directory structure and testing environment.
Error handling for missing files or write errors is included for robustness.

## Task1:
Here's a solution for setting up a basic Flask app with HTML templates, reusable components (header and footer), and multiple routes.

Step 1: Set Up Your Flask Environment
Ensure you have Flask installed. Run:

bash
Copier le code
pip install Flask
Step 2: Create the Flask Application
In the python-server_side_rendering directory, create a file named task_01_jinja.py and add the following code:

python
Copier le code
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
Step 3: Set Up the Templates
In the same directory, create a folder named templates. Inside templates, create the following HTML files:

index.html (Main Page)
html
Copier le code
<!doctype html>
<html lang="en">
<head>
    <title>Home - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
    </ul>

    {% include 'footer.html' %}
</body>
</html>
about.html (About Page)
html
Copier le code
<!doctype html>
<html lang="en">
<head>
    <title>About Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>About Us</h1>
    <p>This page provides information about our application and team.</p>

    {% include 'footer.html' %}
</body>
</html>
contact.html (Contact Page)
html
Copier le code
<!doctype html>
<html lang="en">
<head>
    <title>Contact Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Contact Us</h1>
    <p>Feel free to reach out to us through the contact details provided here.</p>

    {% include 'footer.html' %}
</body>
</html>
Step 4: Create the Header and Footer Templates
These templates will be included in each page, promoting code reusability.

header.html
html
Copier le code
<header>
    <h1>My Flask App</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
</header>
footer.html
html
Copier le code
<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>
Step 5: Run the Flask Application
Now, go to the terminal, navigate to your project directory, and run:

bash
Copier le code
python task_01_jinja.py
The app should be accessible at http://127.0.0.1:5000 with pages:

Home: /
About: /about
Contact: /contact
Explanation
Flask app setup: Defined routes for the main, about, and contact pages.
Template structure: Each page (index.html, about.html, and contact.html) includes header.html and footer.html using {% include %} to avoid code duplication.
Port and Debug Mode: Running on port 5000 with debug=True for easier development.
Resources
Flask Quickstart: Flask Quickstart
Jinja Templating: Jinja Template Inheritance

The error traceback indicates that Flask is unable to find the index.html template. This typically occurs if the template files are not located in the correct directory or if there is a typo in the file or folder names.

Here are some steps to troubleshoot and resolve this:

Check the Template Directory Structure: Ensure that your project directory has a folder named templates and that index.html is located inside this folder. The structure should look like this:

css
Copier le code
project_directory/
├── task_01_jinja.py
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    └── footer.html
Verify File Names and Paths: Make sure the file is named exactly index.html (all lowercase, no typos) and is in the templates folder.

Restart Flask Server: After making changes, restart the Flask server to ensure it loads the correct files.

Check File Permissions: Ensure that Flask has the necessary permissions to read the files in the templates directory.

Run in the Project Root Directory: Start the Flask application from the project root directory (the directory containing task_01_jinja.py). Running the command from outside this directory could lead to path issues.

If you’ve verified all of the above and are still seeing the error, you could try adding a simple debug print statement in task_01_jinja.py to confirm the templates folder is accessible:

python
Copier le code
import os
print("Templates path:", os.path.join(os.getcwd(), 'templates'))
After confirming everything is set up correctly, restart the server and navigate to http://127.0.0.1:5000 to see if the issue is resolved.

## Task2:
Here’s how to implement a dynamic template in Flask using loops and conditionals with Jinja, and to read data from a JSON file.

1. Project Structure
Organize your project directory as follows:

bash
Copier le code
project_directory/
├── task_01_jinja.py          # Flask application file from Task 1
├── task_02_logic.py          # New Flask application file for this task
├── items.json                # JSON data file
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    ├── footer.html
    └── items.html            # New template for the list of items
2. items.json File
Create a file named items.json in your project directory, containing a list of items. Here’s an example:

json
Copier le code
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
To test the empty list condition, modify items.json as follows:

json
Copier le code
{
    "items": []
}
3. task_02_logic.py - Flask Application
In task_02_logic.py, create a new route /items that reads from items.json and passes the data to the items.html template:

python
Copier le code
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/items')
def display_items():
    # Load data from items.json
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []  # Default to an empty list if the file doesn't exist or can't be read

    # Pass items list to the template
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
4. items.html Template
In the templates folder, create items.html with a Jinja loop and conditional statements to display the list dynamically:

html
Copier le code
<!doctype html>
<html lang="en">
<head>
    <title>Items List</title>
</head>
<body>
    <h1>Items List</h1>

    {% if items %}
        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No items found.</p>
    {% endif %}
</body>
</html>
5. Testing the Application
Run the Flask app:

bash
Copier le code
python task_02_logic.py
Visit http://127.0.0.1:5000/items in your browser to test:

When items.json has items, they should display as a list.
When items.json is empty, it should display “No items found.”
Explanation
Route /items: Loads items.json, handles errors, and passes the list to items.html.
Template items.html: Uses {% for %} to loop through items, and {% if %} to display a message if items is empty.
This should provide the desired dynamic rendering functionality in your Flask app.

http://127.0.0.1:5000/items

Items List
No items found.


{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}

{
    "items": []
}

## Task3:






