from google.cloud import vision
from google.cloud.vision import types
import re


def convert(s): 
  
    str1 = " "  
    return(str1.join(s)) 

def fetch(texts):
     return convert(texts[1:])

def fetchText(image_to_open):

    client = vision.ImageAnnotatorClient()

    with open(image_to_open, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    text_response = client.text_detection(image=image)

    texts = [text.description for text in text_response.text_annotations]

    return fetch(texts)
