import pandas as pd
import os
import shutil


def get_image_names_for_empty_category(csv_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Filter the DataFrame to only include rows where the 'category' column is 'Empty'
    empty_category_df = df[df['category'] == 'Empty']

    # Extract the 'image_new_name' column as a list
    image_names = empty_category_df['image_new_name'].tolist()

    # Return the list of image names
    return image_names


if __name__ == '__main__':
    csv_file_path = '/media/mmohseni/ubuntu/storage/ImageTaggerDataLake.csv'
    src_path = '/media/mmohseni/ubuntu/storage/ImageTaggerDataLake'
    des_path = '/home/mmohseni/Desktop/workload/Empty_images'

    image_names = get_image_names_for_empty_category(csv_file_path)
    for i in image_names:
        im_path = os.path.join(src_path, i)
        shutil.copy(im_path, des_path)
