#!/usr/bin/python3
"""
This module provides functionality to serialize a Python dictionary to XML
and deserialize it back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data to.
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string for XML

    # Create an ElementTree and write to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from XML
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text  # XML text is string by default

        return result_dict

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

    except ET.ParseError:
        print(f"Error: The file '{filename}' could not be parsed.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
