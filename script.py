import math
import time
import pytesseract
from PIL import Image
import os

def get_txt():
    start_time = time.time()
    image = Image.open(name_img)
    text = pytesseract.image_to_string(image)
    print(text)

    with open('info.txt', 'w') as file:
        file.write(text)
    end_time = time.time()
    print(f"{round(end_time - start_time, 2)} s")
name_img = input("Insert image name (default is 'thumbnail.png'): ")

if not name_img.strip():
    name_img = "thumbnail.png"

get_txt()