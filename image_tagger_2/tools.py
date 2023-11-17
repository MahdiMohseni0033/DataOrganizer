import os
import shutil
import pandas as pd


def copy_images_by_status(csv_file_path, root_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Create directories for positive and negative images
    positive_dir = os.path.join(root_path, "positive")
    negative_dir = os.path.join(root_path, "negative")
    os.makedirs(positive_dir, exist_ok=True)
    os.makedirs(negative_dir, exist_ok=True)

    # Copy images based on their status
    for index, row in df.iterrows():
        image_name = row["Name"]
        status = row["Status"]

        image_path = os.path.join(root_path, image_name)

        if status == "positive":
            shutil.copy(image_path, positive_dir)
        elif status == "negative":
            shutil.copy(image_path, negative_dir)
        else:
            print(f"Unknown status '{status}' for image '{image_name}'.")

    print("Image copying completed.")


# Example usage:
csv_file_path = "/home/mmohseni/Desktop/workload/other_datasets/TV/TV.csv"
root_path = "/home/mmohseni/Desktop/workload/other_datasets/TV/mother"

copy_images_by_status(csv_file_path, root_path)
