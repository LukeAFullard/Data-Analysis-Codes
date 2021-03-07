%reset -sf
#Reference: https://medium.com/@derrickfwang/printed-and-handwritten-text-extraction-from-images-using-tesseract-and-google-cloud-vision-api-ac059b62a535
#from IPython.display import Image
from matplotlib import pyplot as plt
import pandas as pd, numpy as np
pd.options.display.float_format = '{:,.2f}'.format

from google.cloud import vision
import io

import warnings
warnings.simplefilter("ignore")

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "LOCATION OF YOUR JSON FILE FOR GOOGLE VISION API"
#print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))


def CloudVisionTextExtractor(handwritings):
    # convert image from numpy to bytes for submittion to Google Cloud Vision
    _, encoded_image = cv2.imencode('.png', handwritings)
    content = encoded_image.tobytes()
    image = vision.types.Image(content=content)
    
    # feed handwriting image segment to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)
    
    return response

def getTextFromVisionResponse(response):
    texts = []
    for page in response.full_text_annotation.pages:
        for i, block in enumerate(page.blocks):  
            for paragraph in block.paragraphs:       
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    texts.append(word_text)

    return ' '.join(texts)

import cv2 
#img = cv2.imread('photo1-820x545.jpg') 
#img = cv2.imread('1_f23ONH_H37TXJRO1J-ZjkQ.jpeg') 
img = cv2.imread('handwriting1.jpg') 




# handwritings = segments[2]
#response = CloudVisionTextExtractor(handwritings)
response = CloudVisionTextExtractor(img)
handwrittenText = getTextFromVisionResponse(response)
print(handwrittenText)