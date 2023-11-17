import os
import random
import shutil

def copy_random_images(source_directory, destination_directory, k):
    image_files = get_image_files(source_directory)

    if k > len(image_files):
        print("Warning: 'k' is greater than the number of available images.")
        k = len(image_files)

    random_images = random.sample(image_files, k)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for image_path in random_images:
        image_name = os.path.basename(image_path)
        destination_path = os.path.join(destination_directory, image_name)
        shutil.copy(image_path, destination_path)
        print(f"Image '{image_name}' copied to '{destination_directory}'.")

def get_image_files(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                image_files.append(os.path.join(root, file))
    return image_files

# Example usage:
source_directory = "/home/mmohseni/Desktop/workload/other_datasets/couch/no_couch"
destination_directory = "/home/mmohseni/Desktop/workload/other_datasets/couch/negative"
k = 1300

copy_random_images(source_directory, destination_directory, k)
