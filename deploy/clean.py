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
    if(len(desc.captions) == 0 or desc.captions is None):
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
    if(len(desc.categories) == 0 or desc.categories is None):
        return None
    else:
        results = []
        for d in desc.categories:
            results.append((d.name, d.score))
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
            tmp = (o.object_property,r.x, r.y, r.w, r.h)
            results.append(tmp)
        return results


def get_faces(img):
    global client
    features = ["faces"]
    faces = client.analyze_image(img,features).faces
    if(len(faces) == 0 or (faces is None)):
        return None
    else:
        results = []
        for f in faces:
            r = f.face_rectangle
            results.append((f.age, f.gender, r.left, r.top, r.width, r.height))
        return results
