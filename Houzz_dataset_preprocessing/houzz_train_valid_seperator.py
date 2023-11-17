import shutil
import random
from pathlib import Path
from tqdm import tqdm

root = '/media/mmohseni/ubuntu/storage/Houzz_dataset'
category_names = ['contemprory',
                  'scandinavian',
                  'farmhouse',
                  'industrial',
                  'modern',
                  'traditional']

dataset_path = '/media/mmohseni/ubuntu/storage/Houzz_dataset/Classification_Dataset'

Path(dataset_path).mkdir(parents=True, exist_ok=True)
Path(f"{dataset_path}/train").mkdir(parents=True, exist_ok=True)
Path(f"{dataset_path}/valid").mkdir(parents=True, exist_ok=True)

for cat in category_names:
    src_dir = Path(f"{root}/{cat}")
    train_dir = Path(f"{dataset_path}/train/{cat}")
    valid_dir = Path(f"{dataset_path}/valid/{cat}")

    train_dir.mkdir(parents=True, exist_ok=True)
    valid_dir.mkdir(parents=True, exist_ok=True)

    images = list(src_dir.glob("*.jpg"))
    k = len(images) // 7  # take X% for validation
    valid_images = random.sample(images, k=k)

    print(f'Start to spliting dataset for class : {cat} ')
    print(f'namber of images : {len(images)} ')
    print(f'namber of valid : {k} ')

    for img in tqdm(images):
        if img in valid_images:
            shutil.copy(src=img, dst=valid_dir)
        else:
            shutil.copy(src=img, dst=train_dir)
