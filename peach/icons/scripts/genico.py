from PIL import Image
import glob, os

force_rewrite = False
print("--- [Forced Rewrite] {}".format(force_rewrite))

# .ico sizes
size = 48, 48
_dir = os.path.dirname(os.path.dirname(__file__))
_dir_png = os.path.join(_dir, "500w")
_dir_ico = os.path.join(_dir, "ICO")


rc_data = """IDI_ICON{0} ICON DISCARDABLE "{1}.ico"\n"""

# logging into existing
existing = []
for infile in glob.glob(os.path.join(_dir_ico, "*.ico")):
    file, ext = os.path.splitext(infile)
    filename = os.path.basename(file)
    print("--- [Found File] %s" % filename)
    existing.append(filename)

# getting all the icons from 500w folder
counter = 0
for infile in glob.glob(os.path.join(_dir_png, "*.png")):
    counter += 1
    file, ext = os.path.splitext(infile)
    filename = os.path.basename(file)
    filename = filename.replace("_x500", "")
    
    if not force_rewrite:
        if filename in existing:
            print("--- [Skip File] %s" % filename)
            continue
        
    file = os.path.join(_dir_ico, filename  + ".ico")
    file_rc = os.path.join(_dir_ico, filename  + ".rc")
    
    # Save .ico files
    print("--- [Writing File] %s" % file)
    with Image.open(infile) as im:
        im.save(file, size=size)
    
    # Save .rc files
    print("--- [Writing File] %s" % file_rc)
    with open(file_rc, "w") as rcf:
        rcf.write(rc_data.format(counter, filename))