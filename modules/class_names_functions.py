"""
The following module provides functions for handling class labels and mappings between class IDs and class names. These utility functions can be used for managing class information, transforming data for machine learning models, and converting between different annotation formats. The module includes the following functions:

1. `get_labels(labels_file)`: Reads a labels file and creates a dictionary mapping class IDs to class names.
2. `get_class_name(class_id, labels)`: Retrieves the class name associated with a given class ID.
3. `get_class_code(class_name, labels)`: Retrieves the class ID associated with a given class name.

Each function has its specific utility, which is described below.
"""

def get_labels(labels_file):
    """
    This functions checks if the file 'labels.txt' exists. 
    If not, it generated a .txt file with the generic names for each existing class "class1" to "classN". 
    The users can then change the names later.
    
    **Beware: if defined classes have not been used in the training dataset, they will not appear in this labels.txt file.**

    :param labels_file: 
        - Type: str
        - Description: The path to the 'labels.txt' file which contains the class IDs and corresponding class names.
    
    :return: 
        - Type: dict
        - Description: A dictionary where keys are class IDs (as strings) and values are class names.    
    """
    labels_dict = {}
    with open(labels_file, 'r') as labels:
        for line in labels:
            key, value = line.strip().split(': ')
            key = key.strip("'")
            value = value.strip("'\n")
            labels_dict[key] = value
    
    return labels_dict


def get_class_name(class_id, labels):
    
    """
    This function returns the class name from the class ID. If the class key is not specified, the function returns "class unknown".
    The function will be used in the 'yolo_to_csv' function.
    
    :param class_id: 
        - Type: int or float
        - Description: The ID of the class for which the function should return the corresponding class name. 
        If provided as a float, it will be cast to an integer.
        
    :param labels: 
        - Type: dict
        - Description: A dictionary that maps class IDs (as strings) to class names.
    
    :return: 
        - Type: str
        - Description: The name of the class corresponding to the provided class ID. Returns 'unknown-class' if the ID is not found.
    """
    if not isinstance(class_id, int):
        class_id = int(float(class_id))
        return labels.get(str(class_id), 'unknown-class')

    else:
        return labels.get(str(class_id), 'unknown-class')

def get_class_code(class_name, labels):
    
    """
    This function returns  the ID (key number) from the class name. If the ID key is not specified,
    the function returns "class unknown".
    
    The 'class_id' parameter is  of the class name that will return the ID of the class.
    The parameter will be automatically filled in 'generate_corrected_files' with the results 
    data from Label Studio's corrected csv file.

    :param class_name: 
        - Type: str
        - Description: The name of the class for which the function should return the corresponding class ID.
    
    :param labels: 
        - Type: dict
        - Description: A dictionary that maps class names to class IDs (as strings).
                       This is the reverse mapping of the dictionary used in get_class_name.
    
    :return: 
        - Type: str
        - Description: The ID of the class corresponding to the provided class name. Returns 'unknown-class' if the name is not found.
    """
    
    labels = {value : key for key, value in labels.items()}
    return labels.get(class_name, 'unknown-class')