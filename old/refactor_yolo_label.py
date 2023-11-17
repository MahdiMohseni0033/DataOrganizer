import os
import glob
from tqdm import tqdm

# Define the directory path
dir_path = "/home/sd/Desktop/workload/rename_yolo_file/label"

# Get a list of all .txt files in the directory
txt_files = glob.glob(os.path.join(dir_path, "*.txt"))

# Loop over each file
for file_path in tqdm(txt_files):
    # Read the file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Loop over each line and replace the first number
    for i in range(len(lines)):
        line = lines[i].strip().split()
        first_num = int(line[0])
        if first_num == 2:
            line[0] = "3"
        elif first_num == 3:
            line[0] = "2"
        lines[i] = " ".join(line) + "\n"

    # Write the modified lines back to the file
    with open(file_path, "w") as f:
        f.writelines(lines)