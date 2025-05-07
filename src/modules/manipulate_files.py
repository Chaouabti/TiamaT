"""
The following module provides utility functions for handling JSON annotation files and managing file paths 
within a project structure. These functions are useful for opening and saving JSON files, modifying 
their content, retrieving specific files based on their extension, and filtering out files used in training.

Functions included:
1. open_json_file: Opens a JSON file and returns its content as a dictionary.
2. save_json_file: Saves a dictionary back to a JSON file with a specified path.
3. change_id: Modifies the 'id' field in a JSON file to reflect the file's basename.
4. get_files: Retrieves a list of files with a specified extension from a folder.
5. exclude_training_images: Filters out images used for training from a list of file paths.
"""

import os
import glob
import json

def open_json_file(file_name):
    """
    This function opens corrected annotation files retrieved from Label Studio, in JSON format.
    
    :param file_name: 
        - Type: str
        - Description: Absolute or relative path to the Label Studio annotation file in JSON format.
    
    :return: 
        - Type: dict
        - Description: A dictionary containing the contents of the JSON file.
        """
    
    with open(file_name, 'r') as correction_file:
        return json.load(correction_file)

def save_json_file(file_name, data):
    """
    This function saves the corrected annotation file back to JSON format.

    :param file_name: 
        - Type: str
        - Description: Absolute or relative path to the output JSON file where the corrected data will be saved.

    :param data: 
        - Type: dict
        - Description: A dictionary containing the corrected annotation data to be saved in the JSON file.
    """
    
    with open(file_name, 'w') as corrected_file:
        json.dump(data, corrected_file, indent=4)

def change_id(json_file):
    """
    This function changes the 'id' field in the JSON file to the basename of the file path.

    :param json_file: 
        - Type: str
        - Description: Absolute or relative path to the JSON file whose 'id' field needs to be modified.

    :return: None
    """
    
    data = open_json_file(json_file)
    data['id'] = os.path.basename(json_file)

    with open(json_file, "w") as annotation:
        json.dump(data, annotation, indent=4)
    print(f'Modifications done in {json_file}')

def get_files(folder, extension):
    """
    This function retrieves a list of files with a specific extension from a folder.

    :param folder: 
        - Type: str
        - Description: Absolute or relative path to the folder containing the files.

    :param extension: 
        - Type: str
        - Description: The file extension to filter by (e.g., 'txt', 'jpg'). The extension should not include a dot (e.g., use 'txt' not '.txt').

    :return: 
        - Type: list of str
        - Description: A list of file paths matching the specified extension within the provided folder.
    """
    return glob.glob(os.path.join(folder, f'*.{extension}'))

def exclude_training_images(files, img_use_for_training):
    """
    This function filters out files that correspond to images used for training from a list of files.

    :param files: 
        - Type: list of str
        - Description: A list of file paths to filter, typically corresponding to images or annotations.

    :param img_use_for_training: 
        - Type: list of str
        - Description: A list of image basenames (e.g., 'image1.jpg') that were used for training and should be excluded.

    :return: 
        - Type: list of str
        - Description: A filtered list of file paths excluding those corresponding to images used for training.
    """
    
    return [file for file in files if os.path.basename(file.replace('txt', 'jpg')) not in img_use_for_training]


def load_data_from_files(file_paths):
    """
    This function reads data from a list of file paths and returns the contents as a list of strings. Each file is opened, 
    read line by line, and each line is stripped of any leading or trailing whitespace before being added to the result list.
    
    :param file_paths: 
        - Type: list of str
        - Description: A list of file paths to be read. Each file path should point to a text file containing data.
    
    :return: 
        - Type: list of str
        - Description: A list of strings, where each string is a line from the files specified in `file_paths`.

    This function is useful for consolidating data from multiple text files into a single list, making it easier to process 
    the combined data in subsequent steps.
    """

    data_list = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data_list.append(line.strip())
    return data_list
