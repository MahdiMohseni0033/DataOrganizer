import requests
import json
import csv
import os
import argparse


def download_images(csv_file_name, json_file_name, save_directory):
    # Check if the CSV file already exists
    csv_file_exists = os.path.isfile(csv_file_name)
    file_name = os.path.splitext(os.path.basename(csv_file_name))[0]

    # If the CSV file exists, find the last downloaded image index
    last_index = 0
    if csv_file_exists:
        with open(csv_file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_index = int(row['index'])

    # Read images from JSON file
    with open(json_file_name, 'r') as f:
        images = json.load(f)

    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Create the CSV file and write the header if it doesn't exist
    with open(csv_file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        if not csv_file_exists:
            writer.writerow(['index', 'image_name', 'url', 'tag', 'caption'])

        # Download images starting from the last downloaded index
        for i, image in enumerate(images[last_index:], start=last_index + 1):
            url = image['url']

            image_name = f"{file_name}_image_{i}.jpg"
            image_path = f"{save_directory}/{image_name}"

            try:
                response = requests.get(url)
                response.raise_for_status()

                # Save the image
                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)

                # Write the image data to the CSV file
                writer.writerow([i, image_name, url, image['tag'], image['caption']])

                print(f"Downloaded image {i}: {url}")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading image {i}: {e}")


def create_parser():
    parser = argparse.ArgumentParser(description='Image Downloader')
    parser.add_argument('--csv_file_name', default='/media/sd/ubuntu/storage/Houzz_dataset/chunk_1.csv', help='Path to the CSV file')
    parser.add_argument('--json_file_name', default='chunk_1.json', help='Path to the JSON file')
    parser.add_argument('--save_directory', default='/media/sd/ubuntu/storage/Houzz_dataset/chunk_1', help='Directory to save the images')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    download_images(args.csv_file_name, args.json_file_name, args.save_directory)
