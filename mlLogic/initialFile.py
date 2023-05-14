from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
import warnings
warnings.simplefilter("ignore")
from PIL import Image
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# Loads the pre-trained VisionEncoderDecoderModel from Hugging Face Transformers Hub
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# Loads the pre-trained ViTImageProcessor from Hugging Face Transformers Hub.
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# Loads the pre-trained AutoTokenizer from Hugging Face Transformers Hub.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
#     Sets the device to use the GPU if available, otherwise uses the CPU and moves the model to the specified device.