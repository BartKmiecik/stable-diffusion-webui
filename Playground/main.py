import PIL
from IPython.display import display
from PIL import Image
import requests
import torch
from io import BytesIO

from diffusers import StableDiffusionInpaintPipeline

# img_url = Image.open("Test4.png")
# mask_url = Image.open("Mask0a.png")
#
# init_image = img_url.resize((512, 512))
# mask_image = mask_url.resize((512, 512))
#
#
# image.save('test.png')

request = requests.get('http://127.0.0.1:7860/sdapi/v1/options')
print(request.text)