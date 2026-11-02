###
# Project: project - name
# Purpose: purpose of the script
# Author: author of the script
# E-mail: email adress of the author
# Date: date when the file was created
###

import os

# Create folders --------------------------------------------

root_path = os.getcwd()


folders = ["raw", "code", "data", "text", "documentation", "results"]

for folder in folders:

    print(folder)

    if os.path.isfile(folder):
        print(f"{folder} exists already!")
    else:
        os.mkdir(folder)






### END ######################################################