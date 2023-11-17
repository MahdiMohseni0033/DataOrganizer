import os
import random
import shutil

# Set the source directory path
src_dir = "/media/mmohseni/ubuntu/storage/splitted_images_empty_room"

# Set the destination directory path
dst_dir = "/home/mmohseni/Desktop/workload/Empty_images_filtered"

# Set the number of images to select
k = 2000

# Get a list of all the image filenames in the source directory
image_files = [f for f in os.listdir(src_dir) if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png")]

# Randomly select k images from the list
selected_images = random.sample(image_files, k)

# Copy the selected images to the destination directory
for image in selected_images:
    src_path = os.path.join(src_dir, image)
    dst_path = os.path.join(dst_dir, image)
    shutil.copy(src_path, dst_path)