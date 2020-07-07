from _cffi_backend import typeof
from django.core.paginator import Paginator
from django.shortcuts import render
from monkeylearn import MonkeyLearn
from twitter_handler import TwitterClient
from clean import get_objects
from clean import get_description
from clean import get_categories
from clean import get_faces

handler = TwitterClient()


def main(request):
    ml = MonkeyLearn('d5f9c8516e495eee8123733bf1809849f49ec9ff')
    text = request.POST.get('textfield')
    data2 = [text]
    if (data2[0] == '' or data2[0] is None):
        data2[0] = 'https://twitter.com/R_c_Santos/status/1252678948644945920'
    tweet = handler.get_tweet(data2[0])
    media = tweet.entities.get('media', [])
    hide = ''
    print(data2[0])
    if(len(media) == 0):
        hide = 'hidden'
        img=''
        img_desc=''
    else:
        img = tweet.entities.get('media', [])[0]['media_url']
        img_obj = get_objects(img)
        img_desc = get_description(img)
        img_cat = get_categories(img)
        img_faces= get_faces(img)

        count = 1
        ob = ''
        dc = ''
        cat = ''
        face = ''
        if img_faces is not None:
            count += len(img_faces)
            count+=2
            for f in img_faces:
                face= face + '' + str(f[1].replace('Gender.','')) + ' age ' + str(f[0]) + \
                ' at position ' + str(f[2]) + \
                ',' + str(f[3]) +'\n' 
        if img_obj is not None:
            count += len(img_obj)
            count+=2
            for o in img_obj:
                ob = ob + "" + str(o[0]) + ' at position ' + str(o[1]) + \
                ', ' + str(o[2]) + '\n'
        if img_desc is not None:
            count+=2
            count += len(img_desc)
            for d in img_desc:
                dc = dc + '' + str(d[0]) + ' with ' + '{:.1f}'.format(d[1]*100) + '% ' + 'confidence' + '\n'
        if img_cat is not None:
            count+=2
            count += len(img_cat)
            for c in img_cat:
                cat = cat + "" + str(c[0]) + ' with ' + '{:.1f}'.format(c[1]*100) + '% ' + 'confidence' + '\n' 

        if(dc != ''):
            dc = '\n\t\tImage Description: \n' + dc
        if(ob != ''):
            ob = '\n\t\tObjects in Image: \n' + ob
        if(cat != ''):
            cat = '\n\t\tImage Categories: \n' + cat
        if(face != ''):
            face = '\n\t\tFaces in Image: \n' + face

    try:
        data2[0] = tweet.full_text
        response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=data2
        )
        rw = 'rows=' + str(count)
        tparams = {
            'output': response.body,
            'tweet': data2[0],
            'tag':str(response.body[0]['classifications'][0]['tag_name']),
            'confidence':'{:.1f}'.format(response.body[0]['classifications'][0]['confidence']*100),
            'img': "src="+str(img) ,
            'img_data1': dc,
            'img_data2': cat, 
            'img_data3': face,
            'img_data4': ob,
            'hide': hide,
            'rw': rw,
            'hide2': hide,
            }
    except:
        response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=['teste']
        )

        tparams = {
            'output': response.body,
            'tweet': response.body,
            'hide': 'hidden',
            'hide2': 'hidden',
        }

    return render(request=request, template_name="index.html", context=tparams)

handler = TwitterClient()