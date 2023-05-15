from django.urls import path
from mlLogic import views
app_name = "mlLogic"
urlpatterns = [
    path('caption', views.generate_caption_view, name="generate_caption_view"),
]