from captGendeploy.settings import BASE_DIR
from functionFile import *
import os,shutil
imgRoot = os.path.join(BASE_DIR, 'media','images')
folder_dir = imgRoot
imgList = []
for images in os.listdir(folder_dir):
    imgList.append(images)
img = str(imgList[0])
finalImg = imgRoot+"\\"+img
caption = imgPredictStep([finalImg])
print(*caption)
shutil.rmtree(folder_dir)