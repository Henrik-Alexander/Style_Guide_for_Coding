###
# Project: project - name
# Purpose: purpose of the script
# Author: author of the script
# E-mail: email adress of the author
# Date: date when the file was created
###

import os

# Create folders --------------------------------------------

# Get the root directory of this script
root_path = os.path.dirname(os.path.abspath(__file__))

# Create a list of folder elements
folders = ["raw", "code", "data", "text", "documentation", "results"]

# Function to create a folder in the root directory
def create_folder(folder_name):

    """Create a folder in the project root.

    Args:
        folder_name (str): Name of the folder to create in the root directory.
    """
    folder_path = os.path.join(root_path, folder_name)

    if os.path.exists(folder_path):
        print(f"{folder_name} exists already!")
    else:
        os.mkdir(folder_path)
        print(f"{folder_name} successfully created!")

# Create folders iteratively
for folder in folders:
    create_folder(folder)


### END ######################################################