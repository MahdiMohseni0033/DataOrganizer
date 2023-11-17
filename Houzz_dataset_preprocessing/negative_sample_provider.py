import os
import random
import shutil
from tqdm import tqdm


def copy_random_images(source_dir, destination_dir, k):
    # Get a list of all image files in the source directory
    image_files = [file for file in os.listdir(source_dir) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Randomly select k images (if k is greater than the number of available images, use all images)
    selected_images = random.sample(image_files, min(k, len(image_files)))

    # Copy the selected images to the destination directory
    for image in tqdm(selected_images):
        source_path = os.path.join(source_dir, image)
        destination_path = os.path.join(destination_dir, image)
        shutil.copyfile(source_path, destination_path)


if __name__ == '__main__':
    # Example usage
    source_base_directory = "/media/sd/ubuntu/storage/Houzz_dataset"
    destination_directory = "/home/sd/Desktop/workload/ImageTagger/Binary_classifiers/contemporary/negative"
    k = 2094  # Number of images to randomly select and copy

    style_list = [
        'farmhouse',
        'industrial',
        'modern',
        'scandinavian',
        'traditional'
    ]

    for i in style_list:
        source_directory = os.path.join(source_base_directory, i)
        print(f'\n ============{i}===============/n')
        copy_random_images(source_directory, destination_directory, k)
