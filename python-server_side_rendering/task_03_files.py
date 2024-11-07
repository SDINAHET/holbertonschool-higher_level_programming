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
