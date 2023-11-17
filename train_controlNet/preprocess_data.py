import os
import shutil
import pandas as pd
from tqdm import tqdm


def csv_file_provider():
    # List of CSV files to merge
    root_path = '/media/sd/ubuntu/storage/style_controlnet_dataset'
    csv_files = ['contemprory.csv', 'farmhouse.csv', 'industrial.csv', 'modern.csv', 'scandinavian.csv',
                 'traditional.csv']

    # List of columns to keep from each CSV file
    use_cols = ['image_name', 'tag']

    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame(columns=use_cols)

    # Loop through each CSV file
    for file in csv_files:
        file = os.path.join(root_path, file)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file, usecols=use_cols)

        # Extract the first two words of the tag column and add "make it"
        df['tag'] = df['tag'].str.split(',').str[0:2].str.join(' ').apply(lambda x: f"make it {x}")

        # Append the DataFrame to the merged DataFrame
        merged_df = merged_df.append(df, ignore_index=True)

    # Write the merged DataFrame to a new CSV file

    merged_df.to_csv(os.path.join(root_path, 'merged.csv'), index=False)


def move_images_to_directory():
    """
    Move all image files from the source directory to the destination directory.

    Arguments:
    source_dir -- the path to the directory containing the image files
    dest_dir -- the path to the directory where the image files should be moved to
    """
    # Create the destination directory if it doesn't already exist

    root_path = '/media/sd/ubuntu/storage/Houzz_dataset'
    dest_dir = "/media/sd/ubuntu/storage/style_controlnet_dataset/images"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    source_list = ['contemprory', 'farmhouse', 'industrial', 'modern', 'scandinavian',
                   'traditional']
    for source_dir in source_list:

        source_dir = os.path.join(root_path, source_dir)
        # Loop through all the files in the source directory
        for filename in tqdm(os.listdir(source_dir)):
            filepath = os.path.join(source_dir, filename)

            # Check if the file is an image file (by file extension)
            if os.path.isfile(filepath) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Move the image file to the destination directory
                shutil.copy(filepath, dest_dir)


import pandas as pd


def clean_tags(csv_file, words_to_keep):
    """
    Clean the "tag" column of a CSV file by keeping only certain words.

    Arguments:
    csv_file -- the path to the CSV file containing the "image_name" and "tag" columns
    words_to_keep -- a list of words to keep in the "tag" column

    Returns:
    A new Pandas DataFrame with the "tag" column cleaned
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Loop through each row of the DataFrame
    for i, row in df.iterrows():
        # Split the tag string into a list of words
        tag_words = row['tag'].split()

        # Keep only the words that appear in the words_to_keep list
        tag_words = [word for word in tag_words if word in words_to_keep]

        # Join the remaining words back into a string
        cleaned_tag = ' '.join(tag_words)

        # Update the tag column in the DataFrame with the cleaned version
        df.at[i, 'tag'] = cleaned_tag

    # Return the cleaned DataFrame
    return df


if __name__ == '__main__':
    # csv_file_provider()
    # move_images_to_directory()

    csv_file = '/media/sd/ubuntu/storage/style_controlnet_dataset/output.csv'
    words_to_keep = ["Contemporary", "Kitchen", "Dining", "Room", "Bedroom", "Living", "Farmhouse", "Industrial",
                     "Bathroom", "Modern", "Scandinavian", "Traditional", "make", "it"]

    cleaned_df = clean_tags(csv_file, words_to_keep)

    # Do something with the cleaned DataFrame, e.g. write it to a new CSV file
    cleaned_df.to_csv(csv_file, index=False)
