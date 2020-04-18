import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

endpoint = "https://c-extract.cognitiveservices.azure.com/"
skey = 'c175cadc06ec4622b6e847fe59f2c0f9'


def check(img):
    end_url = endpoint+"vision/v2.1/analyze"
    headers = {'Ocp-Apim-Subscription-Key': skey}
    params = {'visualFeatures': 'Categories,Description,Color'}
    data = {'url': img}
    res = requests.post(end_url, headers=headers, params=params, json=data)
    res.raise_for_status()
    analysis = res.json()
    print(json.dumps(res.json()))
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    # Display the image and overlay it with the caption.
    image = Image.open(BytesIO(requests.get(img).content))
    plt.imshow(image)
    plt.axis("off")
    plt.title(image_caption, size="x-large", y=-0.1)
    plt.show()
