import os
import shutil

Folder_path = '/home/sd/Desktop/corner'
image_path = '/home/sd/Desktop/corner/hard images/11k'


def main():
    im_list = os.listdir(image_path)
    for i, j in enumerate(im_list):

        im_path_ = os.path.join(image_path, j)
        if i < 2000:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part1'))

        elif i > 1999 and i < 4000:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part2'))

        elif i > 3999 and i < 6000:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part3'))

        elif i > 5999 and i < 8000:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part4'))

        elif i > 7999 and i < 10000:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part5'))

        else:
            shutil.copy(im_path_, os.path.join(Folder_path, 'part6'))


if __name__ == '__main__':
    main()
