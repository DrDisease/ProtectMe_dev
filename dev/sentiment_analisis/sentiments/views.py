from _cffi_backend import typeof
from django.core.paginator import Paginator
from django.shortcuts import render
from monkeylearn import MonkeyLearn
from twitter_handler import TwitterClient


client = TwitterClient()


def main(request):
    ml = MonkeyLearn('d5f9c8516e495eee8123733bf1809849f49ec9ff')
    text = request.POST.get('textfield')

    data2 = [text]
    
    testdata = client.get_tweet(data2).full_text

    try:
        response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=testdata
        )

        tparams = {
            'output': response.body,
        }
    except:
        response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=['teste']
        )

        tparams = {
            'output': response.body,
        }

    return render(request=request, template_name="index.html", context=tparams)

