import os
# Define the directory path
directory_path = "C:\\Users\yogesh.gowda.IMANAGE\Desktop"
# Define the name of the folder and document
folder_name = "Imanage_folder"
document_name = "Imanage.txt"
# Create the folder
if not os.path.exists(os.path.join(directory_path, folder_name)):
    os.makedirs(os.path.join(directory_path, folder_name))
# Create the document and write in it
with open(os.path.join(directory_path, folder_name, document_name), "w") as f:
    f.write("This is an automated file created using python script and run through jenkins")
