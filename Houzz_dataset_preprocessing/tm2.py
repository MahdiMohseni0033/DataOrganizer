import os
import random
import shutil

# Set the source directory and destination directory paths
source_dir = '/home/mmohseni/Desktop/workload/room_style/contemprory/negative_mother'
dest_dir = '/home/mmohseni/Desktop/workload/room_style/contemprory/negative'

# Set the number of images to select
k = 453

# Get a list of all the image file names in the source directory
image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Select k random images from the list
selected_images = random.sample(image_files, k)

# Copy the selected images to the destination directory
for image in selected_images:
    shutil.copy(os.path.join(source_dir, image), dest_dir)