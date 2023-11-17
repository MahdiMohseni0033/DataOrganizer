import json
import shutil
from tqdm import tqdm


# Load the JSON data from file
with open('empty_ram_results.json') as f:
    data = json.load(f)

# Loop over each dictionary in the "data" list
for d in tqdm(data['data']):
    # Check if "floor" is in the "model_identified_tags"
    if 'basement' in d['model_identified_tags']:
        # Copy the image file to a desired path
        filepath = d['filepath']
        destination_path = '/home/mmohseni/Desktop/workload/empty_filtered_by_ram/basement'
        shutil.copy(filepath, destination_path)