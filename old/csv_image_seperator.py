import os.path
import shutil

import pandas as pd

path = 'data_seg.csv'


def main():
    df = pd.read_csv(path)

    # Select rows where 'quality status' is 'Bad'
    bad_quality = df[df['quality status'] == 'Bad']

    # Extract the 'image-name' column from the selected rows
    bad_images = bad_quality['Image-name']

    row_path = '/media/sd/ubuntu/sina/old/error_analysis/destination_predict'
    bad_path = '/media/sd/ubuntu/sina/old/error_analysis/bad_seg_predicted'
    for i in bad_images:
        image_path = os.path.join(row_path, i)
        shutil.copy(image_path, bad_path)
        print('Done')


if __name__ == '__main__':
    main()
