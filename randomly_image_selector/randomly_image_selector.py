import os
import random
import pandas as pd
import shutil
from tqdm import tqdm

# Set the source and destination paths
src_path = "/media/mmohseni/ubuntu/storage/splitted_images_empty_room"
dst_path = "/home/mmohseni/Desktop/workload/Empty_images_filtered"

# Set the value of K
K = 2000

# Get a list of all image files in the source folder
image_files = [f for f in os.listdir(src_path) if f.endswith(".jpg")]

# Randomly select K image files
selected_images = random.sample(image_files, K)

# Create a DataFrame to store the old and new names of the selected images
df = pd.DataFrame({"old_name": selected_images})

# Add a new column for the new names of the selected images
df["new_name"] = range(1, K+1)
df["new_name"] = df["new_name"].apply(lambda x: str(x)+".jpg")

# Save the DataFrame as a CSV file
csv_file = os.path.join( "image_mapping.csv")
df.to_csv(csv_file, index=False)

# Copy the selected images to the destination folder with their new names
for i, image_name in tqdm(enumerate(selected_images)):
    old_path = os.path.join(src_path, image_name)
    new_name = str(i+1) + ".jpg"
    new_path = os.path.join(dst_path, new_name)
    shutil.copy2(old_path, new_path)