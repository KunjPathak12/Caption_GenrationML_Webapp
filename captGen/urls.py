from django.urls import path
from captGen import views

app_name = 'captGen'
urlpatterns = [
    path('', views.image_request, name="image-request")]