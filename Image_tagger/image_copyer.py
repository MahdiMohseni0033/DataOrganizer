import os
import shutil
import pandas as pd
from tqdm import tqdm

def copy_images(csv_file_path, source_directory, destination_directory):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Iterate over each row in the DataFrame
    for index, row in tqdm(df.iterrows()):
        old_name = row["Old_Name"]
        new_name = row["New_Name"]

        # Construct the source and destination paths
        source_path = os.path.join(source_directory, old_name)
        destination_path = os.path.join(destination_directory, new_name)

        # Copy the image from source to destination
        shutil.copyfile(source_path, destination_path)

    print("Images copied successfully!")


# Example usage
csv_file_path = "output_t.csv"
source_directory = "/media/mmohseni/ubuntu/storage/style_controlnet_dataset/images"
destination_directory = "/media/mmohseni/ubuntu/storage/style_controlnet_dataset/selected_images"

copy_images(csv_file_path, source_directory, destination_directory)
