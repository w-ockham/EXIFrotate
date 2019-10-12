import os
import sys
from PIL import Image

convert_image = {
  1: lambda img: img,
    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),                              # 左右反転
    3: lambda img: img.transpose(Image.ROTATE_180),                                   # 180度回転
    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),                              # 上下反転
    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_90),  # 左右反転＆反時計回りに90度回転
    6: lambda img: img.transpose(Image.ROTATE_270),                                   # 反時計回りに270度回転
    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_270), # 左右反転＆反時計回りに270度回転
    8: lambda img: img.transpose(Image.ROTATE_90),
}

rotdir = os.path.sep + 'rotated'

file_paths = sys.argv[1:]

for file_path in file_paths:
    img = Image.open(file_path)
    exif = img._getexif()
    if exif:
        orientation = exif.get(0x112,1)
        print('Roate ' + str(orientation)+' : ' + file_path)
        rot_img = convert_image[orientation](img)

        dirname,fname = os.path.split(file_path)
        os.makedirs(dirname + rotdir, exist_ok = True)
        rot_img.save(dirname + rotdir + os.path.sep + fname, quality=95)
