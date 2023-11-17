import os
from tqdm import tqdm
from rembg import remove
from PIL import Image

image_path = '/media/mmohseni/ubuntu/storage/watermark_images/generated_logo_V_1'
output_path = '/media/mmohseni/ubuntu/storage/watermark_images/removed_background_logo_V_1'

im_list = os.listdir(image_path)
for i in tqdm(im_list):
    input_path = os.path.join(image_path,i)
    input = Image.open(input_path)
    output = remove(input)


    output_path1 = os.path.join(output_path,i.split('.')[0]+'.png')
    output.save(output_path1)