import os
import json
import urllib.request
import csv

json_file_path = 'logo.json'
download_directory = '/media/mmohseni/ubuntu/storage/watermark_images/images'
csv_file_path = '/media/mmohseni/ubuntu/storage/watermark_images/log.csv'

# Check if the download directory exists, create it if not
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Check if the CSV file exists, create it with headers if not
csv_headers = ['index', 'url', 'saved_name']

if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Resume from the last saved index
last_index = 0
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            last_index = int(row['index']) + 1

# Download images and save them with renamed file names
with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)

    for i, item in enumerate(data[last_index:], start=last_index):
        url = item['url']
        saved_name = f'watermark_{i}.png'
        file_path = os.path.join(download_directory, saved_name)

        try:
            urllib.request.urlretrieve(url, file_path)
            writer.writerow({'index': i, 'url': url, 'saved_name': saved_name})
            print(f'Downloaded: {url}')
        except Exception as e:
            print(f'Error downloading {url}: {str(e)}')