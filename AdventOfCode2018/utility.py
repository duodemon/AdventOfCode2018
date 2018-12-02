import os


def convert_input_to_string(file_name):
    """The puzzle inputs are usually very long so they are stored in a file and this function reads from the file and
    converts it into a string."""
    if not os.path.exists(file_name):
        raise FileNotFoundError
    with open(file_name, 'r') as f:
        return f.read()