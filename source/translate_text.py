import json
from googletrans import Translator

def translate_text(request):
    translator = Translator(service_urls=['translate.googleapis.com'])
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    in_text = in_nlp['text']
    out_text = translator.translate(in_text,dest='en').text
    response = {"Output Text": out_text}
    return response