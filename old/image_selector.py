import os
import shutil
import cv2

IM_PATH = r'E:\MahdiMohseni\projects\Data_organizer\images'
OK_PATH = r'E:\MahdiMohseni\projects\Data_organizer\ok'
NOT_OK_PATH = r'E:\MahdiMohseni\projects\Data_organizer\not_ok'


def main():
    im_list = os.listdir(IM_PATH)
    for i in range(len(im_list)):

        im_path = os.path.join(IM_PATH, im_list[i])
        im = cv2.imread(im_path)
        cv2.imshow('IM', im)
        key = cv2.waitKey(0)

        # ================= key 1 =========================
        if key == 49:
            print('ok')
            shutil.move(im_path, OK_PATH)
        # ================= key 2 =========================
        elif key == 50:

            print('not ok')
            shutil.move(im_path, NOT_OK_PATH)
        else:

            continue


if __name__ == "__main__":
    main()
