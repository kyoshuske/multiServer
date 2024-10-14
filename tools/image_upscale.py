from PIL import Image, ImageFilter
import os

path = 'assets\\icons\\item'
end_path = path+'\\converted\\'
size = 512, 512
with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".png") and entry.is_file():
            end_file = end_path+entry.name
            im = Image.open(entry.name)
            print('resizing \"'+entry.path+'\"',str(im.size),' --->  '+'\"'+end_file+'\"',str(size),'...')
            im_resized = im.resize(size, resample=Image.BOX)
            # im_sharpened = im_resized.filter(ImageFilter.SHARPEN)
            im_resized.save(end_file,"png")