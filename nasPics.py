from datetime import datetime
import exifread
import os

# mount nas 
# shell script used: sudo mount -t cifs -o sudo mount -t cifs -o username=USERNAME,password=PASSWORD //192.168.0.26/Public/Shared\ Pictures /mnt/nas 

# load file list
target = open('images.txt', 'r')
images = []
images = target.readlines()

# for each
nas_path_prefix = "/mnt/nas"
i = 0

# build path_name
for image in images:
    path_name = nas_path_prefix + images[i][1:-1]
    imgFile = open(path_name, 'rb') # open image file for reading (binary mode)
    tags = exifread.process_file(imgFile) # return Exif tags
    try:
        imgDate = str(tags['EXIF DateTimeOriginal']) # read EXIF DateTimeOriginal
        imgDateDT = datetime.strptime(imgDate, '%Y:%m:%d %H:%M:%S')
        if imgDateDT.year == 2014:
            cmd = "cp %s /home/christopher/dev/opics/calendarPics/%s" % ("'" + path_name + "'", str(imgDateDT.month))
            os.system(cmd)
        i = i + 1
    except: 
        print path_name + " no EXIF data"
        i = i + 1
