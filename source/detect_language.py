import json
from langdetect import detect

def detect_language(request):
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    in_text = in_nlp['text']
    out_text = detect(in_text)
    response = {"Detected language code": out_text}
    return response