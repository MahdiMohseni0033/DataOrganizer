import os
import cv2

Im_path = r'C:\Users\m.mohseni\Desktop\workload\image'
Label_path = r'C:\Users\m.mohseni\Desktop\workload\label'
win_crop_path = r'C:\Users\m.mohseni\Desktop\workload\crropped'


def similar_remover():
    student = "C:\\Users\\User1\\Desktop\\segmentation_datas\\windows_crops_filtered"
    st = os.listdir(student)
    for i in st:
        os.remove(os.path.join(win_crop_path, i))
        print('done')


def cropper(txt_path, image_path):
    source_file = open(txt_path)
    image = cv2.imread(image_path)
    try:
        height, width, channels = image.shape
    except:
        print('no shape info.')
        return 0

    idx = 0
    for line in source_file:
        staff = line.split()
        class_idx = int(staff[0])

        if class_idx == 2:
            idx = idx + 1
            x_center, y_center, w, h = float(staff[1]) * width, float(staff[2]) * height, float(
                staff[3]) * width, float(
                staff[4]) * height
            x1 = round(x_center - w / 2)
            y1 = round(y_center - h / 2)
            x2 = round(x_center + w / 2)
            y2 = round(y_center + h / 2)
            return image[y1:y2, x1:x2], idx
        else:
            continue

    return None, None


def cropper_10percent(txt_path, image_path):
    source_file = open(txt_path)
    image = cv2.imread(image_path)
    try:
        height, width, channels = image.shape
    except:
        print('no shape info.')
        return 0

    idx = 0
    dict_crop = {}
    for line in source_file:
        staff = line.split()
        class_idx = int(staff[0])

        if class_idx == 3:
            idx = idx + 1
            x_center, y_center, w, h = float(staff[1]) * width, float(staff[2]) * height, float(
                staff[3]) * width, float(
                staff[4]) * height

            K_percent = 0.4
            w = (1 + K_percent / 2) * w
            h = (1 + K_percent / 2) * h

            x1 = round(x_center - w / 2)
            if x1 < 0:
                x1 = 0
            y1 = round(y_center - h / 2)
            if y1 < 0:
                y1 = 0
            x2 = round(x_center + w / 2)
            if x2 > width:
                x2 = width
            y2 = round(y_center + h / 2)
            if y2 > height:
                y2 = height

            dict_crop[idx] = image[y1:y2, x1:x2]

            # return image[y1:y2, x1:x2], idx

    # return None, None
    return dict_crop


def main():
    path_list = os.listdir(Label_path)
    for i in path_list:
        txt_path = os.path.join(Label_path, i)
        img_path = os.path.join(Im_path, i.split('.')[0] + '.jpg')
        # cropped_image, idx = cropper(txt_path, img_path)
        cropped_image, idx = cropper_10percent(txt_path, img_path)


        if cropped_image is not None:
            h, w, _ = cropped_image.shape

            if h / w > 5 or w / h > 5 or w * h < 10000:
                continue
            else:
                des_path = os.path.join(win_crop_path, i.split('.')[0] + '_' + str(idx) + '.jpg')
                cv2.imwrite(des_path, cropped_image)



def main2():
    path_list = os.listdir(Label_path)
    for i in path_list:
        txt_path = os.path.join(Label_path, i)
        img_path = os.path.join(Im_path, i.split('.')[0] + '.jpg')
        # cropped_image, idx = cropper(txt_path, img_path)
        # cropped_image, idx = cropper_10percent(txt_path, img_path)
        dict_crop = cropper_10percent(txt_path, img_path)

        if len(dict_crop) > 0:
            for idx in dict_crop.keys():

                h, w, _ = dict_crop[idx].shape

                if h / w > 5 or w / h > 5 or w * h < 10000:
                    continue
                else:
                    des_path = os.path.join(win_crop_path, i.split('.')[0] + '_' + str(idx) + '.jpg')
                    cv2.imwrite(des_path, dict_crop[idx])


if __name__ == '__main__':
    main2()
