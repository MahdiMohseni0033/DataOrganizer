import os
import shutil
from tqdm import tqdm

root_path = '/media/mmohseni/ubuntu/storage/RoomStyles_labels_Operations/buckets'
dst_path = '/media/mmohseni/ubuntu/storage/RoomStyles_labels_Operations/Datalake'
bcuckets = os.listdir(root_path)
for i in bcuckets:
    path = os.path.join(root_path,i)
    for j in tqdm(os.listdir(path)):
        src_path = os.path.join(path,j)
        shutil.copy(src_path,dst_path)
