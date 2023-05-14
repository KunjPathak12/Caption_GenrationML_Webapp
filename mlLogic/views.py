from django.shortcuts import render
import os
from os import *
# get the path/directory
folder_dir = "D:\captGendeploy\media\images"
imgList = []
for images in os.listdir(folder_dir):
    imgList.append(images)
# print(imgList[-1])
# Create your views here.
def generate_caption_view(request):
    pass
