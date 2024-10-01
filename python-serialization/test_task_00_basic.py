#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

def main():
    # Exemple de données à sérialiser
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Sérialiser les données en JSON et les sauvegarder dans un fichier
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Charger et désérialiser les données depuis le fichier JSON
    deserialized_data = load_and_deserialize('data.json')

    # Afficher les données désérialisées
    print("Deserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
