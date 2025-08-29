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

from pathlib import Path


def get_img_folder_training(project_folder):
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
    
    img_folder = Path(project_folder) / 'image_inputs' / 'ground_truth_images'
    return str(img_folder)


def get_img_folder_inference(project_folder):
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
    
    img_folder = Path(project_folder).joinpath('image_inputs', 'eval_images')
    return str(img_folder)


def get_ground_truth_folder_training(project_folder):
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

    ground_truth_folder = Path(project_folder, 'annotations', 'ground_truth')

    return str(ground_truth_folder)


def get_corrections_folder_inference(project_folder:str) -> str:
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
    
    corrections_folder = Path(project_folder).joinpath('annotations', 'prediction_corrections')

    return str(corrections_folder)


def get_results_folder(project_folder:str, yolo_model_folder:str) -> str:
    """
    This function recomposes the path to the folder where results are stored based on the provided YOLO model and image dataset folders.
    
    :param img_dataset_folder: 
        - Type: str
        - Description: Absolute path to the image dataset folder used in the project.

    :param yolo_model_folder: 
        - Type: str
        - Description: Absolute path to the YOLO model folder used in the project.
    
    :return: 
        - Type: str
        - Description: Absolute path to the results folder constructed from the base folder of the project, 
                      the name of the image dataset folder, and the name of the YOLO model folder.
    """
    
    project_name = Path(project_folder).name
    model_name = Path(yolo_model_folder).name
    runs_folder = Path(yolo_model_folder).parent.parent
    results_folder = runs_folder.joinpath('predict', f"{project_name}_{model_name}")
    
    return str(results_folder)


def get_data_folder(project_folder:str) ->str:
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
    
    root = Path(project_folder).parent
    project_name = Path(project_folder).name
    data_folder = root.joinpath(root, 'data', project_name)
    return str(data_folder)

def get_correctedLabels_folder(project_folder:str, yolo_model_folder:str) -> str:
    """
    Returns the string path to the corrected labels folder for a given project and YOLO model.

    Parameters:
    - project_folder: Path to the project directory
    - yolo_model_folder: Path to the trained YOLO model directory

    Returns:
    - Path to the 'correctedLabels' folder as a string object
    """
    project_name = Path(project_folder).name
    model_name = Path(yolo_model_folder).name
    runs_folder = Path(yolo_model_folder).parent.parent
    correctedLabels_folder = runs_folder / 'predict' / f"{project_name}_{model_name}" / 'correctedLabels'
    
    return str(correctedLabels_folder)
