

from PIL import Image
import requests
from io import BytesIO
from controlnet_aux import SamDetector

# load image
path = "x.jpg"


img = Image.open(path).convert("RGB").resize((512, 512))


sam = SamDetector.from_pretrained("ybelkada/segment-anything", subfolder="checkpoints")



processed_image_sam = sam(img)


print('done')
