from azure.cognitiveservices.vision.computervision import \
        ComputerVisionClient as cc
from azure.cognitiveservices.vision.computervision.models import \
        TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import \
        TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import \
        VisualFeatureTypes
from msrest.authentication import \
        CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = 'c175cadc06ec4622b6e847fe59f2c0f9'
endpoint = 'https://c-extract.cognitiveservices.azure.com/'
client = cc(endpoint, CognitiveServicesCredentials(subscription_key))
# Can add function to detect Brands and Logos


def get_description(img):
    global client
    desc = client.describe_image(img)
    if(len(desc) == 0):
        return None
    else:
        results = []
        for d in desc.captions:
            caption = (d.text, d.confidence)
            results.append(caption)
        return results


def get_categories(img):
    global client
    features = ['categories']
    desc = client.analyze_image(img, features)
    if(len(desc) == 0):
        return None
    else:
        results = []
        for d in desc.categories:
            results.append(d.name, d.score)
        return results


def get_objects(img):
    global client
    obj = client.detect_objects(img)
    if(len(obj.objects) == 0):
        return None
    else:
        results = []
        for o in obj.objects:
            # Tupple
            # (x, y, width, height)
            r = o.rectangle
            tmp = (r.x, r.y, r.width, r.height)
            results.append(tmp)
        return results


def get_faces(img):
    global client
    features = ["faces"]
    faces = client.analyze_image(img,features)
    if(len(faces) == 0):
        return None
    else:
        results = []
        for f in faces.faces:
            r = f.face_rectangle
            results.append(f.age, f.gender, r.left, r.top, r.width, r.height)
        return results
