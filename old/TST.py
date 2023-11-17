
import os
import shutil


def XOR():
    """
    it will copy images which is existed in mother directory
    and is not existed in chiled1 directory in chiled2 directory

    """
    mother_path = '/home/sd/Desktop/workload/Detection/bad_images_for_light_detection'
    chiled1_path = '/home/sd/Desktop/workload/Detection/LightDetection_V3'
    chiled2_path = '/home/sd/Desktop/workload/Detection/xor'

    im_list = os.listdir(mother_path)
    for i in im_list:
        if not os.path.exists(os.path.join(chiled1_path, i)):
            shutil.copy(os.path.join(mother_path, i), chiled2_path)
            print('Done')


if __name__=='__main__':
    XOR()