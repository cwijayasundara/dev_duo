import os

""" write a function to save a file to a directory"""


def save_file(file, directory):
    with open(os.path.join(directory, file), "wb") as f:
        f.write(file.getbuffer())
    return os.path.join(directory, file)


def save_file_youtube(content, filename, directory):
    # Check if directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, filename), "w") as f:
        f.write(content)
    return os.path.join(directory, filename)


""" write a function to read a file from a directory"""


def read_file(file):
    with open(file, "rb") as f:
        return f.read()
