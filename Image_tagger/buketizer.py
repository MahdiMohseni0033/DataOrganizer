import os
import random
import shutil
from tqdm import tqdm

def distribute_images(source_directory, k):
    # Get the list of image files in the source directory
    image_files = [file for file in os.listdir(source_directory) if file.endswith(".jpg")]

    # Calculate the number of images to be distributed in each directory
    num_images = len(image_files)
    images_per_directory = num_images // k

    # Shuffle the image files randomly
    random.shuffle(image_files)

    # Create the K new directories
    for i in range(1, k + 1):
        new_directory = f"/home/mmohseni/Desktop/workload/other_datasets/chair/neg_buckets/bucket_{i}"
        os.makedirs(new_directory, exist_ok=True)

        # Copy the appropriate number of images to the new directory
        start_index = (i - 1) * images_per_directory
        end_index = i * images_per_directory
        selected_images = image_files[start_index:end_index]

        for image_file in tqdm(selected_images):
            source_path = os.path.join(source_directory, image_file)
            destination_path = os.path.join(new_directory, image_file)
            shutil.copyfile(source_path, destination_path)

    print("Images distributed successfully!")


# Example usage
source_directory = "/home/mmohseni/Desktop/workload/other_datasets/chair/no_chair"
k = 6

distribute_images(source_directory, k)
