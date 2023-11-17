import cv2
import numpy as np
import json
from itertools import combinations
from shapely.geometry import Polygon


def load_mask_image(image_path):
    """
    Load an image from disk and convert it to grayscale.
    Args:
        image_path: str, path to the image file
    Returns:
        A grayscale image as a NumPy array
    """
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def convert_mask_to_binary(mask, threshold_value):
    """
    Convert a grayscale mask image to a binary image using a threshold value.
    Args:
        mask: ndarray, a grayscale image as a NumPy array
        threshold_value: float, threshold value used to convert the mask image to binary
    Returns:
        A binary image as a NumPy array
    """
    mask[mask > threshold_value] = 255
    mask[mask < threshold_value] = 0
    return cv2.threshold(mask, threshold_value, 1, cv2.THRESH_BINARY)[1]


def generate_polygons_from_contours(contours, epsilon):
    """
    Generates polygons from contours.
    Args:
        contours: list, a list of contour points as NumPy arrays
        epsilon: float, the approximation accuracy parameter
    Returns:
        A list of polygon vertices as NumPy arrays
    """
    print(len(contours))
    polygons = []
    for contour in contours:
        # Fit a polygon to the detected contour with at least 4 points
        polygon = cv2.approxPolyDP(contour, epsilon=epsilon * cv2.arcLength(contour, True), closed=True)
        polygon = polygon.squeeze().tolist()
        # Append polygon to list of polygons
        polygons.append(polygon)
    return polygons


def draw_polygons_on_image(image, polygons, color=(0, 0, 255), thickness=2):
    """
    Draw polygons on an image.
    Args:
        image: ndarray, an input image as a NumPy array
        polygons: list, a list of polygon vertices as NumPy arrays
        color: tuple, color of the polygon edges in BGR format
        thickness: int, thickness of the polygon edges in pixels
    Returns:
        An output image as a NumPy array with polygons drawn on it
    """
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for polygon in polygons:
        points = np.array(polygon).reshape((-1, 1, 2)).astype(np.int32)
        output_image = cv2.polylines(output_image, [points], True, color, thickness=thickness)
    return output_image


def resize_image(image, width, height):
    """
    Resize an image.
    Args:
        image: ndarray, an input image as a NumPy array
        width: int, the desired width of the output image
        height: int, the desired height of the output image
    Returns:
        A resized image as a NumPy array
    """
    return cv2.resize(image, (width, height))


def save_polygons_to_json(polygons, output_path):
    """
    Save a list of polygons to a JSON file.
    Args:
        polygons: list, a list of polygon vertices as NumPy arrays
        output_path: str, path to the output .json file
    """
    data = {}

    for i in range(len(polygons)):
        data[str(i + 1)] = polygons[i]
    with open(output_path, 'w') as f:
        json.dump(data, f)



def get_combinations(input_list, k):
    """
    Returns all possible combinations of k elements from the input_list.

    Args:
    input_list (list): A list of elements to choose from.
    k (int): The number of elements in each combination.

    Returns:
    A list of tuples, where each tuple is a combination of k elements from the input_list.
    """
    return list(combinations(input_list, k))


def calculate_iou(poly1, poly2):
    """
    Calculates the Intersection over Union (IoU) between two polygons.

    Args:
    poly1 (list): A list of (x, y) coordinates that define the vertices of the first polygon.
    poly2 (list): A list of (x, y) coordinates that define the vertices of the second polygon.

    Returns:
    The IoU between the two polygons as a percentage.
    """
    # Convert the polygons to shapely objects
    poly1 = Polygon(poly1).buffer(0)
    poly2 = Polygon(poly2).buffer(0)

    # Calculate the intersection and union of the polygons
    intersection = poly1.intersection(poly2).area
    union = poly1.union(poly2).area

    # Calculate the IoU as the ratio of intersection to union
    iou = (intersection / union) * 100

    return iou


def extract_best_fit_quadrilaterals(polygons):
    """
    Extracts a four-point polygon from each polygon in the input list that has the highest IoU with the original polygon.

    Args:
    polygons (list): A list of polygons, where each polygon is a list of (x, y) coordinates that define its vertices.

    Returns:
    A list of four-point polygons, where each polygon is a list of (x, y) coordinates that define its vertices.
    """
    new_polygons = []

    for sub_poly in polygons:
        max_overlap = 0
        max_polygon = None
        k = 4
        poly_list = get_combinations(sub_poly, k)
        for poly_4p in poly_list:
            poly_4p = list(poly_4p)
            overlap = calculate_iou(sub_poly, poly_4p)
            if overlap > max_overlap:
                max_overlap = overlap
                max_polygon = poly_4p
        new_polygons.append(max_polygon)

    return new_polygons
