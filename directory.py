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
    pass

def save_directory():
    """
    Save the directory table to directory.json.
    Convert FCB objects to dict form before saving.
    """
    pass

def add_file(fcb):
    """
    Insert a new file from directory
    """
    pass

def remove_file(filename):
    """
    Remove the file from directory
    """
    pass

def find_file(filename):
    """
    Return the FCB associated with the filename if it exists
    """
    pass
