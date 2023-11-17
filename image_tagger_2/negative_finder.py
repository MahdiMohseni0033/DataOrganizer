import os
import json
import shutil
import re


def move_images_without_bed(json_file_path, output_directory):
    with open(json_file_path) as file:
        data = json.load(file)

    images_without_bed = [entry["filepath"] for entry in data["data"] if not is_bed_present(entry["model_identified_tags"])]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for image_path in images_without_bed:
        image_name = os.path.basename(image_path)
        output_path = os.path.join(output_directory, image_name)
        shutil.copy(image_path, output_path)
        print(f"Image '{image_name}' moved to '{output_directory}'.")


def is_bed_present(tags):
    pattern = r"\bchair\b"
    matches = re.findall(pattern, tags, flags=re.IGNORECASE)
    return bool(matches)


# Example usage:
json_file_path = "/home/mmohseni/Desktop/workload/other_datasets/ram_results.json"
output_directory = "/home/mmohseni/Desktop/workload/other_datasets/no_chair"

move_images_without_bed(json_file_path, output_directory)
