import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummary"

# .github = we will need this file while CI/CD deployment. Whenever we do the commit, this automatically take our code to the cloud for deployment.
# __init__.py is used to import other python files as a package into the current python code.

list_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/utils/common.py",
                 f"src/{project_name}/logging/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "params.yaml",
                 "app.py",
                 "main.py",
                 "Dockerfile",
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb",
                 ] 


for filepath in list_of_files:
    filepath = Path(filepath)  # Path detects the current OS and based on that it will detect the path 
    filedir, filename = os.path.split(filepath)

    # Create folder  
    if filedir != "": # check weather the file directory is empty

        # 'exist_ok=True' makes sure that if file exists in thhe directory then it will not create the file
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"Creating directory: {filedir}, for the file: {filename}")
    

    # Create file
    
    # checks if the file exist or the size of file. if the size of file is not zero then it will not replace the existing file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open (filepath, 'w') as f:
            pass   # We do not want to write anyything in the file that is why we are jusd creating it in write mode and pass it.

            logging.info(f"Creating emptuy file: {filepath}")

    else:
        logging.info(f"file: {filename} already exist")
