"""
The following module provides utility functions designed to convert bounding box coordinates between different formats used 
in YOLO and Label Studio. The conversion functions facilitate the transformation of relative 
coordinates into absolute coordinates and vice versa.

Functions included:
1. from_relative_coordonates_to_absolute: Converts relative YOLO bounding box coordinates to absolute coordinates.
2. from_ls_to_yolo: Converts Label Studio bounding box coordinates to YOLO format (relative coordinates).
"""

def from_relative_coordinates_to_absolute(x_center, y_center, width, height, img_width, img_height):
    """
    This function transform the relative coordinates of the YOLO bounding box detection into absolute coordinates.
    The absolute coordinates will be used to create the bounding boxes of the detected objects in pixel values.

    :param x_center: 
        - Type: float
        - Description: The relative x coordinate of the center of the bounding box. Value should be between 0 and 1.
    
    :param y_center: 
        - Type: float
        - Description: The relative y coordinate of the center of the bounding box. Value should be between 0 and 1.
    
    :param width: 
        - Type: float
        - Description: The relative width of the bounding box. Value should be between 0 and 1, relative to the image width.
    
    :param height: 
        - Type: float
        - Description: The relative height of the bounding box. Value should be between 0 and 1, relative to the image height.
    
    :param img_width: 
        - Type: int
        - Description: The width of the image in pixels.
    
    :param img_height: 
        - Type: int
        - Description: The height of the image in pixels.
    
    :return: 
        - Type: tuple of int
        - Description: A tuple containing four absolute coordinates (upper_left_x, upper_left_y, width, height) 
                       of the bounding box in pixels.
    """
    
    abs_x_center = x_center * img_width
    abs_y_center = y_center * img_height
    abs_width = width * img_width
    abs_height = height * img_height

    upper_left_x = abs_x_center - (abs_width / 2)
    upper_left_y = abs_y_center - (abs_height / 2)

    absolute_coordinates = int(upper_left_x), int(upper_left_y), int(abs_width), int(abs_height)
    
    return absolute_coordinates


def from_ls_to_yolo(x, y, width, height):
    """
    This function converts annotation coordinates from Label Studio format to YOLO format (relative coordinates).

    :param x: 
        - Type: float
        - Description: The Label Studio format 'x' coordinate of the upper-left corner of the bounding box. 
                       Value is in percentage relative to the image dimensions.

    :param y: 
        - Type: float
        - Description: The Label Studio format 'y' coordinate of the upper-left corner of the bounding box. 
                       Value is in percentage relative to the image dimensions.
    
    :param width: 
        - Type: float
        - Description: The Label Studio format 'width' of the bounding box in percentage relative to the image dimensions.
    
    :param height: 
        - Type: float
        - Description: The Label Studio format 'height' of the bounding box in percentage relative to the image dimensions.
    
    :return: 
        - Type: tuple of str
        - Description: A tuple containing the YOLO format relative coordinates (x_center, y_center, width, height) as strings.
                       These values are in the range [0, 1] and are relative to the image dimensions.
    """
    
    yolo_width = width / 100
    yolo_height =  height / 100
    yolo_x = (x + width / 2) / 100
    yolo_y = (y + height / 2) / 100
    
    return str(yolo_x), str(yolo_y), str(yolo_width), str(yolo_height)