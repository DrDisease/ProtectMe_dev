from _cffi_backend import typeof
from django.core.paginator import Paginator
from django.shortcuts import render
from monkeylearn import MonkeyLearn


def main(request):
    ml = MonkeyLearn('d5f9c8516e495eee8123733bf1809849f49ec9ff')
    text = request.POST.get('textfield')

    data2 = [text]

    try:
        response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=data2
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

