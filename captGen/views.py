from django.shortcuts import redirect, render
from captGen.forms import *
from .models import uploadImage


def image_request(request):
    if request.method == 'POST':
        form = userImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'images.html', {'form': form, 'img_obj': img_object})
    else:
        form = userImageForm()
    return render(request, 'images.html', {'form': form})
