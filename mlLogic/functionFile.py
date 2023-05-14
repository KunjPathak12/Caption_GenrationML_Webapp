from initialFile import *

max_length = 16
num_beams = 4
# Sets the maximum length and number of beams to use during caption generation.
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def imgPredictStep(imagePaths):
    images =[]
    for imgPath in imagePaths:
        selectedImage = Image.open(imgPath)
        # let's check if it's rgb or not if it's not let's convert it to one!
        if selectedImage.mode !="RGB":
            selectedImage = selectedImage.convert(mode="RGB")
        images.append(selectedImage)
    pixel_values = feature_extractor(images = images, return_tensors="pt").pixel_values
    # print(type(pixel_values),pixel_values)
    pixel_values = pixel_values.to(device)
    outputIds = model.generate(pixel_values, **gen_kwargs)

    captions = tokenizer.batch_decode(outputIds, skip_special_tokens=True)
    captions = [caption.strip() for caption in captions]
    return captions
'''This function  takes a list of image paths as input and returns a list of predicted captions. Further, 
it Opens and converts each image to RGB mode. Also, it extracts the pixel values using the feature_extractor.
It Generates a caption using the pre-trained model and tokenizes the output_ids to obtain the predicted captions. 
Also, it removes any special tokens and strips leading/trailing whitespace from the predicted captions. 
And, finally returns a list of predicted captions.'''