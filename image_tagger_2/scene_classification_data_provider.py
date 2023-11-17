import os
import random
import shutil

def create_dataset(root_dir, target_dir):
    # Get a list of all directories in the root directory
    directories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

    for directory in directories:
        source_path = os.path.join(root_dir, directory)
        positive_path = os.path.join(target_dir, f"Dataset_{directory}", "positive")
        negative_path = os.path.join(target_dir, f"Dataset_{directory}", "negative")

        # Create the positive and negative directories
        os.makedirs(positive_path, exist_ok=True)
        os.makedirs(negative_path, exist_ok=True)

        # Copy images from the source directory to the positive directory
        image_files = os.listdir(source_path)
        for image_file in image_files:
            source_image_path = os.path.join(source_path, image_file)
            shutil.copy(source_image_path, positive_path)

        # Determine the number of images in the positive directory
        num_positive_images = len(image_files)

        # Get a list of all directories except the current one
        other_directories = [d for d in directories if d != directory]

        # Randomly select images from other directories and copy them to the negative directory
        for _ in range(num_positive_images):
            random_directory = random.choice(other_directories)
            random_directory_path = os.path.join(root_dir, random_directory)
            random_image = random.choice(os.listdir(random_directory_path))
            source_random_image_path = os.path.join(random_directory_path, random_image)
            shutil.copy(source_random_image_path, negative_path)

# Provide the root directory containing the subdirectories with images
root_directory = "/home/mmohseni/Desktop/workload/other_datasets/scene_classification/valid"

# Specify the target directory where the dataset structure will be created
target_directory = "/home/mmohseni/Desktop/workload/other_datasets/scene_classification/valid_target"

create_dataset(root_directory, target_directory)
