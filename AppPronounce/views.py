from django.shortcuts import render
from .cmudict import DisplayCMU
from googletrans import Translator
import os
import sys
import urllib.request


def translate(request):
    keyword = request.GET['keyword']
    pronounce = DisplayCMU(keyword)

    translator = Translator()
    translated = translator.translate(keyword, src='en', dest='ko').text

    beautifulVoice = voice(keyword) + '.mp3'

    return render(request, 'translate.html', {'original' : keyword, 'pronounce' : pronounce, 'translated' : translated, 'beautifulVoice' : beautifulVoice })

def voice(keyword):
    client_id = "t0phmewyi5"
    client_secret = "lm56DMcXHIhLOR3ScvyfedenC5OEzaHIxtURXGSa"
    encText = urllib.parse.quote(keyword)
    data = "speaker=clara&speed=0&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
   
    # create audio file
    if(rescode==200):
        print("TTS mp3 저장")
        response_body = response.read()
        abspath = os.path.abspath('../')
        with open('static/' + keyword+'.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

    return keyword
    