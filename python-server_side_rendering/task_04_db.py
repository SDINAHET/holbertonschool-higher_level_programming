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
