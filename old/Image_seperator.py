import os
import cv2
import pandas as pd

csv_file_name = "Image_csv.csv"
folder_path = r"C:\Users\m.mohseni\Desktop\light_detection\visulized"


def image_provider(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(filename)

    return image_list


def csv_checker(image_list, csv_file_name):
    if not os.path.exists(csv_file_name):
        df = pd.DataFrame({'Image-name': image_list, 'quality status': 'None'})
        df.to_csv(csv_file_name, index=False)
        return 0

    else:
        df = pd.read_csv(csv_file_name)
        for i, row in df.iterrows():
            if row['quality status'] == "None":
                return i

        return None


def show_images(image_list, csv_file_name, start=0):
    df = pd.read_csv(csv_file_name)
    for i in range(start, len(df)):
        row = df.loc[i]
        image_name = row['Image-name']
        quality_status = row['quality status']
        if quality_status == "None":
            image_path = os.path.join(folder_path, image_name)
            image = cv2.imread(image_path)
            cv2.imshow(image_name, image)
            key = cv2.waitKey(0)
            if key == ord('g'):
                quality_status = "Good"
            elif key == ord('b'):
                quality_status = "Bad"
            cv2.destroyAllWindows()
            df.at[i, 'quality status'] = quality_status
            df.to_csv(csv_file_name, index=False)
            if key == ord('q'):
                break


def main():
    image_list = image_provider(folder_path)
    pointer = csv_checker(image_list, csv_file_name)
    show_images(image_list, csv_file_name, start=pointer)
    print("Done!!!", pointer)


if __name__ == "__main__":
    main()