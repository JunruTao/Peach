import PIL
import os
from PIL import Image

# 1. get subdirs
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
this_dir = os.path.realpath(".")
dirs = [os.path.join(this_dir, f) for f in dirs]
renamed_prf = "r2K_"

for d in dirs:
    for file in os.listdir(d):
        if not file.startswith("preview") and not file.startswith(renamed_prf):
            renamed = renamed_prf + file
            f_img_out = os.path.join(d, renamed)
            f_img = os.path.join(d, file)
            print(f_img)
            # img = Image.open(f_img)
            # img = img.resize((2160, 2160))
            # img.save(f_img)
            os.rename(f_img, f_img_out)