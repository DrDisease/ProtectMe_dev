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
from json_templates import azure_template

from array import array
import os
from PIL import Image
import sys
import time
from conf import AZURE_ENDPOINT
from conf import AZURE_KEY

client = cc(AZURE_ENDPOINT, CognitiveServicesCredentials(AZURE_KEY))
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



if __name__ == "__main__":
    img_url = "https://i1.wp.com/espalhafactos.com/wp-content/uploads/2019/05/praca.jpg"
    cat = get_categories(img_url)
    desc = get_description(img_url)
    faces = get_faces(img_url)
    objects = get_objects(img_url)
    #print(azure_template(cat,desc,faces,objects))
    print(cat)
    print(desc)
    print(faces)
    print(objects)