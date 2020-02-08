import re

from PIL import Image
import os
import sys


final_size = 50

def resize(folder):
    path = folder+"/"
    dirs = os.listdir(path)
    for item in dirs:
        # print(item)
        if item == '.DS_Store' or ".mp4" in item:
            continue
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            size = im.size
            # if size[0] > final_size or size[1] > final_size:
            if not re.search(r'[0-9]{1,4}p',f):
                ratio = float(final_size) / max(size)
                new_image_size = tuple([int(x*ratio) for x in size])
                im = im.resize(new_image_size, Image.ANTIALIAS)
                new_im = Image.new("RGB", (final_size, final_size))
                new_im.paste(
                    im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
                # print(f)
                # os.system("rm *"+f+"*")
                new_im.save(f + '_'+str(final_size)+'p'+'.jpg', 'JPEG', quality=90)



# for folder in os.listdir("dataset"):
#     resize("dataset/"+folder)
    
# resize("examples")
resize("dataset_tana/tana")