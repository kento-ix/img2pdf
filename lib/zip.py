import zipfile
import os

def open_and_deletezip(directory_path):
    #get all of the file n the directory
    files = os.listdir(directory_path)

    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(directory_path, file)
            extract_to = os.path.splitext(zip_file_path)[0]
            os.makedirs(extract_to, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

            os.remove(zip_file_path)
