import os
import shutil
import pandas as pd

# Read the CSV file into a pandas DataFrame
root_path = '/home/mmohseni/Desktop/workload/14020405 - Output/traditional'
os.chdir(root_path)
df = pd.read_csv('output.csv')

# Create the 'positive' and 'negative' directories if they don't exist
if not os.path.exists('positive'):
    os.makedirs('positive')
if not os.path.exists('negative'):
    os.makedirs('negative')

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Get the image name and status for the current row
    name = row['Name']
    status = row['Status']

    # If the status is 'positive', copy the image to the 'positive' directory
    if status == 'positive':
        shutil.copy(f'Images/{name}', 'positive')
    # If the status is 'negative', copy the image to the 'negative' directory
    elif status == 'negative':
        shutil.copy(f'Images/{name}', 'negative')