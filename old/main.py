import cv2
import os
import shutil
import random


def data_spliter_based_labels():
    Label_path = r'C:\Users\m.mohseni\Desktop\light_detection\labels'
    DES_PATH = r'C:\Users\m.mohseni\Desktop\light_detection\chiled'
    Image_path = r'C:\Users\m.mohseni\Desktop\light_detection\mother'

    labels_name = os.listdir(Label_path)
    for i in range(len(labels_name)):
        im_name = labels_name[i].split('.')[0] + ".jpg"
        im_path = os.path.join(Image_path, im_name)
        shutil.move(im_path, DES_PATH)

    print('done')


def filter_image_based_imsize():
    PATH = "C:\\Users\\User1\\Desktop\\worhflow\\light detection dataset\\V1\\straightforward datas"
    DES_PATH = "C:\\Users\\User1\Desktop\\worhflow\\light detection dataset\\V1\\low_res_images"

    a = os.listdir(PATH)
    for i in range(len(a)):

        im_path = os.path.join(PATH, a[i])
        im = cv2.imread(im_path)
        if im.shape[0] < 640 or im.shape[1] < 640:
            shutil.move(im_path, DES_PATH)
    print('done')


def data_name_changer():
    PATH = "C:\\Users\\User1\\Desktop\\worhflow\\light detection dataset\\V1\\straightforward datas"
    Des_sortedD = "C:\\Users\\User1\\Desktop\\worhflow\\light detection dataset\\V1\\sorted_name"

    a = os.listdir(PATH)
    for i in range(len(a)):
        im_path = os.path.join(PATH, a[i])
        im = cv2.imread(im_path)
        saved_name = str(i) + ".jpg"
        filename = os.path.join(Des_sortedD, saved_name)
        cv2.imwrite(filename, im)

    print('done')


def train_test_spliter():
    Label_path = "C:\\Users\\User1\\Desktop\\final dataset\\labels"
    val_images = "C:\\Users\\User1\\Desktop\\final dataset\\valid_images"
    val_labels = "C:\\Users\\User1\\Desktop\\final dataset\\valid_labels"
    Image_path = "C:\\Users\\User1\\Desktop\\final dataset\\images"


    labels_name = os.listdir(Label_path)
    Valid_Num = int(len(labels_name)*(1-0.2))
    valid_set = random.choices(labels_name, k=Valid_Num)

    for i in range(len(valid_set)):
        la_path = os.path.join(Label_path, valid_set[i])
        shutil.move(la_path, val_labels)

        im_name = valid_set[i].split('.')[0] + ".jpg"
        im_path = os.path.join(Image_path, im_name)
        shutil.move(im_path, val_images)
        print("MOVE")


def split_dataset():
    label_dir =  r'C:\Users\m.mohseni\Desktop\whole_light_data\ann'
    valid_image_dir = r'C:\Users\m.mohseni\Desktop\whole_light_data\im_val'
    valid_label_dir = r'C:\Users\m.mohseni\Desktop\whole_light_data\ann_val'
    image_dir = r'C:\Users\m.mohseni\Desktop\whole_light_data\image'

    label_files = os.listdir(label_dir)
    num_valid = int(len(label_files) * 0.15)
    valid_files = random.sample(label_files, num_valid)

    for label_file in valid_files:
        src_label_path = os.path.join(label_dir, label_file)
        dst_label_path = os.path.join(valid_label_dir, label_file)
        shutil.move(src_label_path, dst_label_path)

        image_file = label_file.replace('.txt', '.jpg')
        src_image_path = os.path.join(image_dir, image_file)
        dst_image_path = os.path.join(valid_image_dir, image_file)
        shutil.move(src_image_path, dst_image_path)


def similar_remover():

    mother_path = r"E:\MahdiMohseni\work_flow\mother"
    chiled_path = r"E:\MahdiMohseni\work_flow\chiled"
    st = os.listdir(chiled_path)
    for i in st:
        os.remove(os.path.join(mother_path, i))
        print('done')


def compare_directories(dir1, dir2, output_file):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    not_exist = files1.symmetric_difference(files2)

    with open(output_file, 'w') as file:
        for name in not_exist:
            file.write(name + '\n')

if __name__ == '__main__':
    # similar_remover()
    # data_spliter_based_labels()
    split_dataset()

