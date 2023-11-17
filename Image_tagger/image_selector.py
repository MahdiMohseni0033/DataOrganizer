import os
import random
import pandas as pd


def select_images(root_path, directory_dict, csv_file_path):
    # Create a DataFrame from the existing CSV file or create a new one if it doesn't exist
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
    else:
        df = pd.DataFrame(columns=["New_Name", "Old_Name"])

    # Get the last assigned number from the "New_Name" column
    # last_assigned_number = df["New_Name"].str.extract(r"(\d+)").astype(int).max()
    # Get the last assigned number from the "New_Name" column
    last_assigned_number = df["New_Name"].str.extract(r"(\d+)").astype(int).max().item()

    # If no numbers found or DataFrame is empty, start numbering from 1
    if pd.isna(last_assigned_number):
        last_assigned_number = 0
    else:
        last_assigned_number = last_assigned_number.item()

    # Iterate over the directories and select K random images from each directory
    for directory, k in directory_dict.items():
        directory_path = os.path.join(root_path, directory)
        if os.path.isdir(directory_path):
            files = os.listdir(directory_path)
            image_names = [file for file in files if file.endswith(".jpg")]

            # Filter out already selected images
            old_names = df["Old_Name"].tolist()
            image_names = [name for name in image_names if name not in old_names]

            # Randomly select K images
            selected_images = random.sample(image_names, min(k, len(image_names)))

            # Assign new names based on the last assigned number
            new_names = [str(last_assigned_number + i + 1) + ".jpg" for i in range(len(selected_images))]

            # Add selected images to the DataFrame and update the CSV file
            new_df = pd.DataFrame({"New_Name": new_names, "Old_Name": selected_images})
            df = df.append(new_df)
            df.to_csv(csv_file_path, index=False)

            # Update the last assigned number
            last_assigned_number += len(selected_images)

    return df


root_path = "/media/mmohseni/ubuntu/storage/Houzz_dataset"
directory_dict = {"contemprory": 500,
                  "farmhouse": 1500,
                  "industrial": 2500,
                  "modern": 1500,
                  "scandinavian": 1500,
                  "traditional": 1500
                  }

csv_file_path = "output_t.csv"

result_df = select_images(root_path, directory_dict, csv_file_path)
