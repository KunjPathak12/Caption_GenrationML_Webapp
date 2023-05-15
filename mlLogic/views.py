from django.shortcuts import render
import requests
from mlLogic.driver import *
def generate_caption_view(request):
    if request.method == "POST":
        image_caption = mkOutput()
        # print(image_caption)
        return render(request,'caption.html',{'caption' : image_caption})
    else:
        return render(request, 'images.html')
# def show_caption(request):
#     # Render the template with a caption variable passed in
#     return render(request, 'caption.html', {'caption': ''})