Python-server_side_rendering

## Task0:
To create this templating program, let's break down the requirements step-by-step. We will use Python's string manipulation and file handling capabilities to read a template, process data for multiple attendees, and output personalized invitation files. Here’s how we can implement each part of this task:

Steps to Implement generate_invitations:
Validate Input Types and Content: Ensure template is a string and attendees is a list of dictionaries. If either is incorrect, log an error message and exit.
Handle Empty Inputs: Check if template or attendees list is empty. Log a message and exit if so.
Process Each Attendee: `Loop over each dictionary in attendees`, and `use placeholders to substitute values from the dictionary`, using "N/A" if a value is missing.
`Write Output Files`: Create output files in a sequence (e.g., `output_1.txt`, `output_2.txt`, etc.) for each processed invitation.
Code Implementation
Here's the complete Python code for the `generate_invitations function`:

```python
#!/usr/bin/python3
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
```

### Explanation of Key Sections:
Input Validation: We check if template is a string and `attendees is a list of dictionaries`. If not, an error message is printed and the function exits.
Empty Template and Attendees Check: If the template or attendees are empty, it logs a message and stops the function.
`Generating Invitations: For each attendee, we replace placeholders ({name}, {event_title}, {event_date}, and {event_location}) in the template. If any key is missing, it substitutes "N/A".`
`Writing Files: Each processed template is written to a file named output_X.txt, where X is the index of the attendee in the list.`
Example Template File: template.txt
Save this content in a file named template.txt:

```plaintext
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```
Example Data and Main File for Testing
Save the following code in your main file (for example, main.py) to test the program:

```python
#!/usr/bin/python3
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
```

### Testing the Program:
Run `main.py` in your Python environment.
This should read template.txt, process the attendees list, and generate files named `output_1.txt`, `output_2.txt`, etc.
Each output file should contain a personalized invitation, with missing data fields replaced by `"N/A"`.
Expected Output in Files

`output_1.txt` for Alice:

```plaintext
Hello Alice,

You are invited to the Python Conference on 2023-07-15 at New York.

We look forward to your presence.

Best regards,
Event Team
```

`output_2.txt` for Bob:

```plaintext
Hello Bob,

You are invited to the Data Science Workshop on 2023-08-20 at San Francisco.

We look forward to your presence.

Best regards,
Event Team
```

`output_3.txt` for Charlie (missing event_date):

```plaintext
Hello Charlie,

You are invited to the AI Summit on N/A at Boston.

We look forward to your presence.

Best regards,
Event Team
```

Notes
Ensure template.txt exists in the same directory or update the path as needed.
Modify the file paths and names as per your directory structure and testing environment.
Error handling for missing files or write errors is included for robustness.

## Task1:
Here's a solution for setting up a basic Flask app with HTML templates, reusable components (header and footer), and multiple routes.

### Step 1: Set Up Your Flask Environment
Ensure you have Flask installed. Run:

```bash
pip install Flask
```
### Step 2: Create the Flask Application
In the python-server_side_rendering directory, create a file named `task_01_jinja.py` and add the following code:

```python
#!/usr/bin/python3
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
```

### Step 3: Set Up the Templates
In the same directory, create a folder named templates. Inside templates, create the following HTML files:

`index.html (Main Page)`
```html
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
```

`about.html (About Page)`
```html
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
```
`contact.html (Contact Page)`
```html
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
```
### Step 4: Create the Header and Footer Templates
These templates will be included in each page, promoting code reusability.

`header.html`
```html
<header>
    <h1>My Flask App</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
</header>
```
`footer.html`
```html
<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>
```
### Step 5: Run the Flask Application
Now, go to the terminal, navigate to your project directory, and run:

```bash
python task_01_jinja.py
```
The app should be accessible at http://127.0.0.1:5000 with pages:

Home: /
About: /about
Contact: /contact

### Explanation
Flask app setup: Defined routes for the main, about, and contact pages.
Template structure: Each page (index.html, about.html, and contact.html) includes header.html and footer.html using {% include %} to avoid code duplication.
Port and Debug Mode: Running on port 5000 with debug=True for easier development.
Resources
Flask Quickstart: Flask Quickstart
Jinja Templating: Jinja Template Inheritance

The error traceback indicates that Flask is unable to find the index.html template. This typically occurs if the template files are not located in the correct directory or if there is a typo in the file or folder names.

Here are some steps to troubleshoot and resolve this:

Check the Template Directory Structure: Ensure that your project directory has a folder named templates and that index.html is located inside this folder. The structure should look like this:

```css
project_directory/
├── task_01_jinja.py
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    └── footer.html
```
Verify File Names and Paths: Make sure the file is named exactly `index.html` (all lowercase, no typos) and is in the templates folder.

Restart Flask Server: After making changes, restart the Flask server to ensure it loads the correct files.

Check File Permissions: Ensure that Flask has the necessary permissions to read the files in the templates directory.

Run in the Project Root Directory: Start the Flask application from the project root directory (the directory containing task_01_jinja.py). Running the command from outside this directory could lead to path issues.

If you’ve verified all of the above and are still seeing the error, you could try adding a simple debug print statement in task_01_jinja.py to confirm the templates folder is accessible:

```python
#!/usr/bin/python3
import os
print("Templates path:", os.path.join(os.getcwd(), 'templates'))
```
After confirming everything is set up correctly, restart the server and navigate to `http://127.0.0.1:5000` to see if the issue is resolved.

## Task2:
Here’s how to implement a dynamic template in Flask using loops and conditionals with `Jinja`, and to read data from a JSON file.

1. Project Structure
Organize your project directory as follows:

```bash
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
```

2. `items.json` File
Create a file named `items.json` in your project directory, containing a list of items. Here’s an example:

```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```
To test the empty list condition, modify `items.json` as follows:

```json
{
    "items": []
}
```

3. `task_02_logic.py` - Flask Application
In `task_02_logic.py`, `create a new route /items` that reads from `items.json` and passes the data to the `items.html template`:

```python
#!/usr/bin/python3
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
```

4. `items.html` Template
In the `templates folder`, `create items.html with a Jinja loop` and conditional statements to `display the list dynamically`:

```html
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
```
5. Testing the Application
Run the Flask app:

```bash
python task_02_logic.py
```
Visit http://127.0.0.1:5000/items in your browser to test:

When items.json has items, they should display as a list.
When items.json is empty, it should display “No items found.”
Explanation
`Route /items: Loads items.json, handles errors, and passes the list to items.html.`
`Template items.html: Uses {% for %} to loop through items, and {% if %} to display a message if items is empty.`
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
Here's how you can set up this task in Flask to display data from either a `JSON` or `CSV` file based on a query parameter, with filtering and error handling.

### Step 1: Create Data Files
Create `products.json` in your project directory:

```json
[
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
```
Create `products.csv` in your project directory:

```csv
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

### Step 2: Create product_display.html Template
In your `templates folder`, create product_display.html to display the data in a table. It will handle the display of products and any error messages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Display</title>
</head>
<body>
    <h1>Product Display</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% else %}
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
            </tr>
            {% for product in products %}
            <tr>
                <td>{{ product["name"] }}</td>
                <td>{{ product["category"] }}</td>
                <td>{{ product["price"] }}</td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
```

### Step 3: Implement Flask Application in task_03_files.py
In `task_03_files.py`, create the Flask app with the necessary route and file-reading logic.

```python
#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])  # Convert id to int for consistency
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # Read data from JSON or CSV based on the source parameter
    if source == 'json':
        try:
            products = read_json_file('products.json')
        except FileNotFoundError:
            error = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
        except FileNotFoundError:
            error = "CSV file not found."
    else:
        error = "Wrong source. Please specify 'json' or 'csv'."

    # Filter products by ID if provided
    if not error and product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            error = "Product not found."

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 4: Test Your Application
Run the Flask app and test with various URLs:

Display all products from JSON:

```bash
http://127.0.0.1:5000/products?source=json
Display all products from CSV:
```

```bash
http://127.0.0.1:5000/products?source=csv
Display a specific product by ID (e.g., id=1) from JSON:
```

```bash
http://127.0.0.1:5000/products?source=json&id=1
Display a product with a nonexistent ID:
```
```bash
http://127.0.0.1:5000/products?source=json&id=999
Display with an invalid source:
```

```bash
http://127.0.0.1:5000/products?source=xml
The app should render the data correctly in the template, and display error messages for any missing files, incorrect sources, or unfound product IDs.
```


## Task4
Here’s how to extend your Flask application to include SQLite as an additional data source:

### Step 1: Set Up the SQLite Database
Create a script to initialize your `SQLite database (products.db)` and populate it with some sample data.

Create and Run `create_products_db.py`:

```python
#!/usr/bin/python3
# create_products_db.py
import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
```
Run this script to `create products.db` and populate it with sample data.

```bash
python initialize_db.py
```

### Step 2: Update the Flask Application (task_04_db.py)
Add a function to fetch data from the `SQLite database` and integrate it with the existing Flask application.

task_04_db.py:

```python
#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read from JSON file
def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to read from CSV file
def read_csv_file(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])  # Convert id to int for consistency
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

# Function to read from SQLite database
def read_sqlite_db():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            products.append(product)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # Choose data source based on the 'source' query parameter
    if source == 'json':
        try:
            products = read_json_file('products.json')
        except FileNotFoundError:
            error = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
        except FileNotFoundError:
            error = "CSV file not found."
    elif source == 'sql':
        products = read_sqlite_db()
        if not products:
            error = "Database error or no data found."
    else:
        error = "Wrong source. Please specify 'json', 'csv', or 'sql'."

    # Filter products by ID if provided
    if not error and product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            error = "Product not found."

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3: Test Your Application
Start the Flask server:

```bash
python task_04_db.py
```
Test URLs:

Display all products from JSON:

```bash
http://127.0.0.1:5000/products?source=json
```

j'ai
http://127.0.0.1:5000/products?source=json
Product Display
JSON file not found.


Display all products from CSV:

```bash
http://127.0.0.1:5000/products?source=csv
```

j'ai
http://127.0.0.1:5000/products?source=csv
Product Display
CSV file not found.

Display all products from SQLite:

```bash
http://127.0.0.1:5000/products?source=sql
```

j'ai
http://127.0.0.1:5000/products?source=sql
Product Display
Wrong source. Please specify 'json' or 'csv'.

Display a specific product by ID (e.g., id=1) from SQLite:

```bash
http://127.0.0.1:5000/products?source=sql&id=1
```

j'ai
http://127.0.0.1:5000/products?source=sql&id=1
Product Display
Wrong source. Please specify 'json' or 'csv'.

Display with an invalid source:

```bash
http://127.0.0.1:5000/products?source=xml
```

j'ai
http://127.0.0.1:5000/products?source=xml
Product Display
Wrong source. Please specify 'json' or 'csv'.


### Explanation of Code Changes

SQLite Database Handling:

The read_sqlite_db function connects to products.db, fetches all rows from the Products table, and formats them into dictionaries that can be passed to the template.
Error Handling:

If the source is invalid, an error message is displayed.
If the SQLite database encounters an error or lacks data, the function handles this gracefully and informs the user.
Template Rendering:

The same template, `product_display.html`, is used for all sources to maintain consistency.
This completes the integration of `SQLite with JSON and CSV sources`. Let me know if you have questions or encounter any issues!
