###
# Project: project - name
# Purpose: purpose of the script
# Author: author of the script
# E-mail: email adress of the author
# Date: date when the file was created
###

# List folders
folders <- c("raw", "code", "data", "text", "documentation", "results")

# Create the folders in the current working directory
lapply(folders, function(folder_name) if (!dir.exists(folder_name)) dir.create(folder_name))

### END ######################################################