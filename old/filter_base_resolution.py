import os
import shutil
from PIL import Image


def f1():
    # Get the directory path from user input
    directory_path = r'C:\Users\m.mohseni\Desktop\V3_light\images'

    # Create the image_filtered directory
    image_filtered_dir = r'C:\Users\m.mohseni\Desktop\V3_light\image_filtered'
    os.makedirs(image_filtered_dir, exist_ok=True)

    # image_filterd_list =[]
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is an image
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):

            # Open the image and get its size
            with Image.open(file_path) as img:
                width, height = img.size

                # Check if the image resolution is more than 700
                if width > 800 or height > 800:
                    # Copy the file to the image_filtered directory
                    shutil.copy(file_path, image_filtered_dir)


def f2():
    image_filtered_path = r'C:\Users\m.mohseni\Desktop\V3_light\image_filtered'
    ann_filtered_path = r'C:\Users\m.mohseni\Desktop\V3_light\annotation_filtered'

    im_list = os.listdir(image_filtered_path)
    ann_list = []
    for i in im_list:
        ann_list.append(i.split('.')[0] + '.txt')

    for i in ann_list:
        file_path = os.path.join(r'C:\Users\m.mohseni\Desktop\V3_light\annotation', i)
        shutil.copy(file_path, ann_filtered_path)


if __name__ == '__main__':
    f2()
