from PIL import Image
from PIL.ExifTags import TAGS
import os
from json_templates import pil_template
import filetype
import string
import random

red = '\033[91m'
green = '\033[92m'
endc = '\033[0m'


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def extract_metadata(img):
    if img is not None:
        kind=filetype.guess('image.jpg')
        if kind is None:
            print(str(red) + "Invalid PIL Image Type" + str(endc))
            return ""
        elif kind.mime != 'image/jpeg':
            print(str(red) + "Invalid PIL Image Type" + str(endc))
            return ""
        exifdata = img.getexif()
        lst = []
        for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
        # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            meta = (f"{tag:25}: {data}")
            lst.append(meta)
        return lst
    else:
        return ""


if __name__ == "__main__":
    name = 'image.jpg'
    os.system('wget -O image.jpg ' + 'https://live.staticflickr.com/4561/38054606355_26429c884f_b.jpg')
    img = Image.open(name)
    lst = extract_metadata(img)
    print(pil_template(lst))
    os.system('rm image.jpg')

