import os
import json
import csv
import requests
import pandas as pd


# Check if the CSV file exists
csv_filename = '/media/mmohseni/ubuntu/storage/watermark_images/image_data.csv'
images_path = '/media/mmohseni/ubuntu/storage/watermark_images/images'
if not os.path.isfile(csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['index', 'url', 'saved_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Function to download and save an image
def download_image(url, saved_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(saved_name, 'wb') as file:
            file.write(response.content)

# Load the JSON data


# Specify the path to your JSON file
json_file_path = "logo.json"

# Load the JSON file
try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    print("JSON file loaded successfully.")
    # Now, 'data' contains the JSON data as a Python dictionary or list, depending on the JSON structure.
    # You can access and work with the data as needed.
except FileNotFoundError:
    print(f"JSON file not found at {json_file_path}. Please provide the correct file path.")
except json.JSONDecodeError:
    print(f"Failed to parse JSON in {json_file_path}. Check the JSON file for syntax errors.")


# Check for existing downloaded images
downloaded_images = os.listdir()
watermark_images = [img for img in downloaded_images if img.startswith("watermark_")]

# Create a CSV file or load an existing one
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['index', 'url', 'saved_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
else:
    existing_data = pd.read_csv(csv_filename)
print(f'the number of images === > {len(data)}')
# Start downloading and updating the CSV
for index, item in enumerate(data):
    url = item["url"]
    saved_name = f"watermark_{index}.jpg"
    saved_name = os.path.join(images_path,saved_name)

    # Check if this image has already been downloaded
    if saved_name in watermark_images:
        print(f"Image {index} already downloaded.")
    else:
        download_image(url, saved_name)
        print(f"Downloaded image {index}")

    # Update the CSV with the information
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ['index', 'url', 'saved_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'index': index, 'url': url, 'saved_name': saved_name})

print("Download and CSV update completed.")
