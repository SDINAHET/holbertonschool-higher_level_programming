#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

def main():
    csv_file = "data_02.csv"

    # Convertir le fichier CSV en JSON
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data_02.json")
    else:
        print(f"Failed to convert {csv_file} to JSON")

if __name__ == "__main__":
    main()
