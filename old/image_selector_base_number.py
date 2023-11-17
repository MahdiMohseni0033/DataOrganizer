import os.path
import shutil


def main():
    source_path = '/media/sd/ubuntu/sina/old/error_analysis/bad_images_for_light_segmentation'
    destination_path = '/home/sd/Desktop/LightSegmentation_V3.2.0(s1)'

    images_list = os.listdir(source_path)
    NUM_IMG = 5000
    counter = 0

    for i in images_list:
        image_path = os.path.join(source_path, i)
        shutil.copy(image_path, destination_path)
        if counter == NUM_IMG-1:
            break
        counter = counter + 1
        print('Done')


if __name__ == '__main__':
    main()
