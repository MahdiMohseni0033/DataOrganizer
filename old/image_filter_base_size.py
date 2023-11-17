import cv2
import os
import shutil


def filter_image_based_imsize(src_path: str, dst_path: str, max_size: int = 640):
    """
    Filter images based on their size and move the large images to a destination folder.

    Args:
        src_path (str): Path to the folder containing the source images.
        dst_path (str): Path to the destination folder where the filtered images will be moved.
        max_size (int): Maximum size of the image, default is 640.

    Returns:
        None
    """
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"{src_path} does not exist.")

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for file_name in os.listdir(src_path):
        file_path = os.path.join(src_path, file_name)

        if os.path.isfile(file_path):
            img = cv2.imread(file_path)

            if img is None:
                print(f"Skipping {file_path} as it is not a valid image file.")
                continue

            height, width, channels = img.shape

            if height > max_size or width > max_size:
                shutil.move(file_path, os.path.join(dst_path, file_name))

    print('Done')


if __name__ == '__main__':
    # Set source and destination paths here
    src_path = "row/image/path"
    dst_path = "high_res/filtered/image/path"

    filter_image_based_imsize(src_path, dst_path)
