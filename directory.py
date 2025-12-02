import json
import os
from fcb import FCB

# use a json because it's easier to work with, no binary parsing
DIRECTORY_PATH = "directory.json"
directory = {}
"""
example directory tree:
root {
    "type": "folder",
    "contents": {
        "file1.txt": {
            "type": "file",
            "size": 1024,
            "start_block": 0,
            "created": 1234567890,
            "modified": 1234567890
        },
        ....
    }
}
"""

def load_directory():
    """
    Load directory.json and rebuild the directory table.
    If file not found, start with empty directory.
    """
    global directory
    try:
        with open(DIRECTORY_PATH, "r") as f:
            directory = json.load(f)
    except FileNotFoundError:
        directory = {
            "type": "folder",
            "contents": {}
        }

def save_directory():
    """
    Save the directory table to directory.json.
    Convert FCB objects to dict form before saving.
    """
    def convert_fcbs(node):
        if isinstance(node, FCB):
            return node.to_dict()
        elif isinstance(node, dict):
            converted = {}
            for key, value in node.items():
                converted[key] = convert_fcbs(value)
            return converted
        else:
            return node
    
    converted_directory = convert_fcbs(directory)
    
    with open(DIRECTORY_PATH, "w") as f:
        json.dump(converted_directory, f, indent=2)

def add_file(fcb):
    """
    Insert a new file from directory
    """
    if "contents" not in directory:
        directory["contents"] = {}
    
    directory["contents"][fcb.name] = fcb

def remove_file(filename):
    """
    Remove the file from directory
    """
    if "contents" in directory and filename in directory["contents"]:
        del directory["contents"][filename]

def find_file(filename):
    """
    Return the FCB associated with the filename if it exists
    """
    if "contents" in directory and filename in directory["contents"]:
        file_data = directory["contents"][filename]
        
        if isinstance(file_data, FCB):
            return file_data
        
        if isinstance(file_data, dict):
            return FCB.from_dict(file_data)
    
    return None
