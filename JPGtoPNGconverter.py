import os
from PIL import Image
4
image_folder = r'C:\Users\mayas\PycharmProjects\scripting_with_python\images'
output_folder = r'C:\Users\mayas\PycharmProjects\scripting_with_python\new_images'

for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}/{filename}')
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print("all done!")





