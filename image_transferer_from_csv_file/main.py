import pandas as pd
import shutil
import os
from tqdm import tqdm


def image_transferer():
    csv_path = "/media/mmohseni/ubuntu/Datasets/new_inpainting/state.csv"
    im_src_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/contemprory'
    mask_src_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/mask'

    dst_im_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/im_processed'
    dst_mask_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/mask_processed'

    df = pd.read_csv(csv_path)
    x = df[df['Status'] == "processed"]
    processed_images = list(x['Name'])

    for i in tqdm(processed_images):
        im_path = os.path.join(im_src_path, i)
        mask_path = os.path.join(mask_src_path, i.split('.')[0] + '_mask.png')

        shutil.copy(im_path, dst_im_path)
        shutil.copy(mask_path, dst_mask_path)

    print('Done')


def convert_png_to_jpg(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return

    # Get the list of files in the directory
    files = os.listdir(directory_path)

    for file in files:
        # Check if the file has a .png extension
        if file.endswith('.png'):
            # Build the full path of the file
            old_file_path = os.path.join(directory_path, file)

            # Change the file extension to .jpg
            new_file_path = os.path.join(directory_path, os.path.splitext(file)[0] + '.jpg')

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file}' to '{os.path.basename(new_file_path)}'.")


def x():
    src_im_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/im_processed'
    src_mask_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/mask_processed'

    dst_im_path = '/media/mmohseni/ubuntu/Datasets/OR_Dataset/V3.0.0/img'
    dst_mask_path = '/media/mmohseni/ubuntu/Datasets/OR_Dataset/V3.0.0/mask'

    im_list = os.listdir(src_im_path)
    for i in tqdm(im_list):
        im_path = os.path.join(src_im_path, i)
        mask_path = os.path.join(src_mask_path, i.split('.')[0] + '_mask.jpg')
        shutil.copy(im_path, dst_im_path)
        shutil.copy(mask_path, dst_mask_path)


if __name__ == '__main__':
    # # Example usage:
    # directory_path = '/media/mmohseni/ubuntu/Datasets/new_inpainting/mask_processed'
    # convert_png_to_jpg(directory_path)
    x()
