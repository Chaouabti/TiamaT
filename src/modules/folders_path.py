"""
The following module provides functions for retrieving and recomposing the paths of specific folders 
within a given project structure. These paths are used to access the folders containing annotated 
images, non-annotated images, ground_truth, corrections, and results.

Functions included:
1. img_folder_training: Returns the path to the folder containing annotated images.
2. img_folder_inference: Returns the path to the folder containing non-annotated images.
3. ground_truth_folder_training: Returns the path to the folder containing annotation files.
4. corrections_folder_inference: Returns the path to the folder containing correction files.
5. get_results_folder: Constructs and returns the path to the results folder based on the provided YOLO model and image dataset folders.
"""

import os


def img_folder_training(project_folder):
    """
    This function recomposes the path to the folder containing the annotated images, 
    corresponding to the 'annotated_images' folder in the structure.

    :param project_folder: 
        - Type: str
        - Description: Absolute path to the folder named after your project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the 'annotated_images' folder within the project folder.
    """
    
    img_folder = os.path.join(project_folder, 'image_inputs', 'ground_truth_images')
    return img_folder


def img_folder_inference(project_folder):
    """
    This function recomposes the path to the folder containing the non-annotated images, 
    corresponding to the 'eval_images' folder in the structure.

    :param project_folder: 
        - Type: str
        - Description: Absolute path to the folder named after your project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the 'eval_images' folder within the project folder.
    """
    
    img_folder = os.path.join(project_folder, 'image_inputs', 'eval_images')
    return img_folder


def ground_truth_folder_training(project_folder):
    """
    This function recomposes the path to the folder containing the annotation files, 
    corresponding to the 'ground_truth' folder in the structure.

    :param project_folder: 
        - Type: str
        - Description: Absolute path to the folder named after your project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the 'ground_truth' folder within the project folder.
    """

    ground_truth_folder = os.path.join(project_folder, 'annotations', 'ground_truth')
    return ground_truth_folder


def corrections_folder_inference(project_folder):
    """
    This function recomposes the path to the folder containing the correction files, 
    corresponding to the 'corrections' folder in the structure.

    :param project_folder: 
        - Type: str
        - Description: Absolute path to the folder named after your project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the 'corrections' folder within the project folder.
    """
    
    corrections_folder = os.path.join(project_folder, 'annotations', 'prediction_corrections')
    return corrections_folder


def get_results_folder(yolo_model_folder, img_dataset_folder):
    """
    This function recomposes the path to the folder where results are stored based on the provided YOLO model and image dataset folders.

    :param yolo_model_folder: 
        - Type: str
        - Description: Absolute path to the YOLO model folder used in the project.
    
    :param img_dataset_folder: 
        - Type: str
        - Description: Absolute path to the image dataset folder used in the project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the results folder constructed from the base folder of the project, 
                      the name of the image dataset folder, and the name of the YOLO model folder.
    """
    
    base_folder = os.path.dirname(os.path.dirname(yolo_model_folder))
    img_folder_name = img_dataset_folder.split('/')[-3]
    model_name = os.path.basename(yolo_model_folder)
    return os.path.join(base_folder, 'predict', f"{img_folder_name}_{model_name}")


def get_data_folder(project_folder):
    """
    This function recomposes the path to the data folder corresponding to the provided project folder
    by replacing the project folder name with 'data' in the path.

    :param project_folder:
        - Type: str
        - Description: Absolute path to the project folder.
    :return:
        - Type: str
        - Description: Absolute path to the data folder constructed by replacing the
                       project folder name in the provided path with 'data'.
    """
    
    project_name = project_folder.split('/')[-1]
    data_folder = project_folder.replace(project_name, 'data')
    return data_folder
