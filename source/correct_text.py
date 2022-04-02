import json
from textblob import TextBlob

def correct_text(request):
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    in_text = in_nlp['text']
    out_text = str(TextBlob(in_text).correct())
    response = {"Output Text": out_text}
    return response