import json
from textblob import TextBlob

def sentiment_analysis(request):
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    in_text = in_nlp['text']
    out_sub = TextBlob(in_text).sentiment.subjectivity
    out_sent = TextBlob(in_text).sentiment.polarity

    if out_sub==0:
        out_sub_txt = "Absent"
    elif out_sub>=0 and out_sub<=0.33:
        out_sub_txt = "Low"
    elif out_sub>=0.34 and out_sub<=0.66:
        out_sub_txt = "Average"
    elif out_sub>=0.67 and out_sub<=1:
        out_sub_txt = "High"
        
    if out_sent<0:
        out_sent_txt = "Negative"
    elif out_sent==0:
        out_sent_txt = "Neutral"
    elif out_sent>0:
        out_sent_txt = "Positive"

    num_response = {"Subjectivity": out_sub, "Sentiment": out_sent}
    text_response = {"Subjectivity": out_sub_txt, "Sentiment": out_sent_txt}
    response = {"Number Response": num_response, "Text Response": text_response}
    return response