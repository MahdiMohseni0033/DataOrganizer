import cv2
import shutil
import numpy as np
import os
import pandas as pd
from PIL import Image
import random


def mask_preparetor():
    """
    Move labelIds mask files from a mother directory to a child directory,
    and change their name.

    Returns:
        None
    """
    # cityscape folder path
    MOTHER_PATH = '/home/sd/Desktop/workload/Segmentation/raw_masks'

    # approprate mask for visualized path
    CHILD_PATH = '/home/sd/Desktop/workload/Segmentation/filtered_masks'

    gt_list = os.listdir(MOTHER_PATH)
    for i in gt_list:
        if i.split('.')[0].split('_')[-1] == 'labelIds':
            path = os.path.join(MOTHER_PATH, i)
            shutil.move(path, CHILD_PATH)
            print('Done')

    gt_list = os.listdir(CHILD_PATH)
    for i in gt_list:
        path = os.path.join(CHILD_PATH, i)
        x = i.split('.')
        new_name = x[0] + '.png'
        new_path = os.path.join(CHILD_PATH, new_name)
        os.rename(path, new_path)
        print('done')


def data_spliter_based_labels():
    Label_path = '/home/sd/Desktop/workload/Segmentation/filtered_masks'
    DES_PATH = '/home/sd/Desktop/workload/Segmentation/image_with_masks'
    Image_path = '/home/sd/Desktop/workload/Segmentation/Images_mother'

    labels_name = os.listdir(Label_path)
    for i in range(len(labels_name)):
        im_name = labels_name[i].replace('_gtFine_labelIds.png', '.jpg')
        im_path = os.path.join(Image_path, im_name)
        shutil.copy(im_path, DES_PATH)

    print('done')


def image_mask_exist_checker():
    """
    Check if the corresponding mask file exists for each image file in a directory and
    create a Pandas DataFrame to store the image and mask data. Save the DataFrame as
    an Excel file and a filtered DataFrame containing only the rows where the 'Status'
    column is 'NOT OK' as a separate Excel file.

    Returns:
        None

    """
    # Define the directories containing the images and masks
    image_dir = '/home/sd/Desktop/workload/Images_chiled'
    mask_dir = '/home/sd/Desktop/workload/masks'

    # Get the list of image files in the image directory
    image_files = os.listdir(image_dir)

    # Initialize an empty list to store the data
    data = []

    # Loop through the image files and get their corresponding masks
    for image_file in image_files:
        # Get the image name without extension
        image_name = os.path.splitext(image_file)[0]
        # Open the image file and get its size
        with Image.open(os.path.join(image_dir, image_file)) as img:
            image_shape = img.size
        # Check if the corresponding mask file exists
        mask_file = image_name.split('.')[0] + '_gtFine_labelIds.png'
        if os.path.exists(os.path.join(mask_dir, mask_file)):
            # Open the mask file and get its size
            with Image.open(os.path.join(mask_dir, mask_file)) as mask:
                mask_shape = mask.size
            # Record the data in the list
            if image_shape == mask_shape:
                status = 'OK'
            else:
                status = 'NOT OK'
            data.append([image_name, image_shape, mask_file, mask_shape, status])
        else:
            print(f"No mask file found for {image_file}")

    # Create a pandas dataframe from the data
    df = pd.DataFrame(data, columns=['Image Name', 'Image Shape', 'Mask Name', 'Mask Shape', 'Status'])
    not_ok_df = df.loc[df['Status'] == 'NOT OK']

    # save
    df.to_excel('data.xlsx', index=False)
    not_ok_df.to_excel('Not_Ok_Data.xlsx', index=False)

    print('done')


def XOR():
    """
    it will copy images which is existed in mother directory
    and is not existed in chiled1 directory in chiled2 directory

    """
    mother_path = '/home/sd/Desktop/workload/tmp/image'
    chiled1_path = '/home/sd/Desktop/workload/tmp/chiled_1'
    chiled2_path = '/home/sd/Desktop/workload/tmp/chiled_2'

    im_list = os.listdir(mother_path)
    for i in im_list:
        if not os.path.exists(os.path.join(chiled1_path, i)):
            shutil.copy(os.path.join(mother_path, i), chiled2_path)
            print('Done')


def seg_spliter_val_train():
    # Set the paths to the image and annotation folders
    image_folder = "/media/sd/ubuntu/storage/workload/chiled"
    annotation_folder = "/media/sd/ubuntu/storage/workload/labels_filter"

    # Set the paths to the train and validation directories
    train_dir = "media/sd/ubuntu/storage/workload/train"
    val_dir = "media/sd/ubuntu/storage/workload/val"
    img_dir = "img_dir"
    ann_dir = "ann_dir"

    # Set the validation split percentage
    val_split_percent = 15

    # Get a list of all the image filenames
    image_filenames = os.listdir(image_folder)

    # Get the total number of images
    num_images = len(image_filenames)

    # Calculate the number of images for the validation set
    num_val_images = int(num_images * (val_split_percent / 100))

    # Shuffle the image filenames
    random.shuffle(image_filenames)

    # Split the image filenames into training and validation sets
    train_image_filenames = image_filenames[num_val_images:]
    val_image_filenames = image_filenames[:num_val_images]

    # Create the train and validation directories and their subdirectories
    os.makedirs(os.path.join(train_dir, img_dir), exist_ok=True)
    os.makedirs(os.path.join(train_dir, ann_dir), exist_ok=True)
    os.makedirs(os.path.join(val_dir, img_dir), exist_ok=True)
    os.makedirs(os.path.join(val_dir, ann_dir), exist_ok=True)

    # Copy the training images and annotations to the train directory
    for image_filename in train_image_filenames:
        image_index = image_filename.split("_")[0]
        image_path = os.path.join(image_folder, image_filename)
        ann_path = os.path.join(annotation_folder, f"{image_index}_gtFine_labelTrainIds.png")
        shutil.copy(image_path, os.path.join(train_dir, img_dir))
        shutil.copy(ann_path, os.path.join(train_dir, ann_dir))

    # Copy the validation images and annotations to the val directory
    for image_filename in val_image_filenames:
        image_index = image_filename.split("_")[0]
        image_path = os.path.join(image_folder, image_filename)
        ann_path = os.path.join(annotation_folder, f"{image_index}_gtFine_labelTrainIds.png")
        shutil.copy(image_path, os.path.join(val_dir, img_dir))
        shutil.copy(ann_path, os.path.join(val_dir, ann_dir))


def rename_image_to_cityscape_format():
    PATH = '/home/sd/Desktop/workload/tmp/chiled_2'
    gt_list = os.listdir(PATH)
    for i in gt_list:
        path = os.path.join(PATH, i)
        x = i.split('.')
        new_name = x[0] + '_leftImg8bit.png'
        new_path = os.path.join(PATH, new_name)
        os.rename(path, new_path)
        print('done')


def rename_masks_to_cityscape_format():
    PATH = '/home/sd/Desktop/workload/Segmentation/masks'
    gt_list = os.listdir(PATH)
    for i in gt_list:
        path = os.path.join(PATH, i)
        new_path = os.path.join(PATH,  i.replace('_gtFine_labelIds.png', '_gtFine_labelTrainIds.png'))
        os.rename(path, new_path)
        print('done')


def mask_maker():
    # Set up the paths to the input and output folders
    input_folder = '/home/sd/Desktop/workload/tmp/chiled_2'
    output_folder = '/home/sd/Desktop/workload/tmp/chiled_2_mask'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Loop through all the JPEG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            # Read in the JPEG image
            image = Image.open(os.path.join(input_folder, filename))

            # Create a new blank image with the same size as the input image
            mask = Image.new('L', image.size, 0)

            # Save the new image with the modified name to the output folder
            mask_filename = filename.replace('.jpg', '_gtFine_labelIds.png')
            mask.save(os.path.join(output_folder, mask_filename))


def label_visualizer():
    Im_path = '/home/sd/Desktop/workload/Segmentation/image_with_masks'
    Mask_path = '/home/sd/Desktop/workload/Segmentation/filtered_masks'
    Dst = '/home/sd/Desktop/workload/Segmentation/visualized'

    pallet = {'Red': [255, 0, 0],  # -----> curtain_high
              'Green': [0, 255, 0],  # -----> curtain_low
              'Blue': [0, 0, 255],  # -----> glass_high
              'Yellow': [255, 255, 0],  # -----> glass_low
              'Purple': [255, 0, 255],  # -----> shutter_high
              'Orange': [255, 128, 0],  # -----> shutter_low
              'Gray': [128, 128, 128],  # ----->  Background

              }
    im_list = os.listdir(Im_path)
    name_list = [i.split('.')[0] for i in im_list]
    c = 0
    for i in name_list:
        im = cv2.imread(os.path.join(Im_path, i + '.jpg'))
        if os.path.exists(os.path.join(Dst, i + 'segmented.jpg')):
            print('exist')
        else:
            mask = cv2.imread(os.path.join(Mask_path, i + '_gtFine_labelIds.png'))

            H, W, _ = im.shape

            for h in range(H):
                for w in range(W):
                    if mask[h, w, 0] == 0:
                        mask[h, w, :] = pallet['Gray']

                    elif mask[h, w, 0] == 1:
                        mask[h, w, :] = pallet['Red']

                    # elif mask[h, w, 0] == 2:
                    #     mask[h, w, :] = pallet['Green']
                    #
                    # elif mask[h, w, 0] == 3:
                    #     mask[h, w, :] = pallet['Blue']
                    #
                    # elif mask[h, w, 0] == 4:
                    #     mask[h, w, :] = pallet['Yellow']
                    #
                    # elif mask[h, w, 0] == 5:
                    #     mask[h, w, :] = pallet['Purple']
                    #
                    # elif mask[h, w, 0] == 6:
                    #     mask[h, w, :] = pallet['Orange']

            im2 = cv2.addWeighted(im, 0.5, mask, 0.5, 0)
            traget_name = i + 'segmented.jpg'
            output_path = os.path.join(Dst, traget_name)
            cv2.imwrite(output_path, cv2.cvtColor(im2, cv2.COLOR_RGB2BGR))
            print(c)
            c = c + 1


if __name__ == '__main__':
    # mask_preparetor()
    # data_spliter_based_labels()
    # image_mask_exist_checker()
    # XOR()
    # label_visualizer()
    # mask_maker()
    # rename_image_to_cityscape_format()
    rename_masks_to_cityscape_format()
