from flask import Flask,request,jsonify
from source.correct_text import correct_text
from source.translate_text import translate_text
from source.detect_language import detect_language
from source.sentiment import sentiment_analysis
from source.words_stats import words_stats
from source.input_validation import validate_in

app = Flask(__name__)

#sentiment analysis - polarity and subjectivity in numbers and in text format
@app.route('/sentiment_analysis', methods = ['POST'])
def SentimentAnalysis():
    if validate_in(request):
       response = sentiment_analysis(request)
       return jsonify(response),200
    else:
        return jsonify("Validation error. Input is not in expected format."),400
    
#correct spelling of text
@app.route('/correct_text', methods = ['POST'])
def CorrectText():
    if validate_in(request):
        response = correct_text(request)
        return jsonify(response),200
    else:
        return jsonify("Validation error. Input is not in expected format."),400

#language detection
@app.route('/detect_language', methods = ['POST'])
def DetectLanguage():
    if validate_in(request):
        response = detect_language(request)
        return jsonify(response),200
    else:
        return jsonify("Validation error. Input is not in expected format."),400

#translate non-english language into english
@app.route('/translate_text', methods = ['POST'])
def TranslateText():
    if validate_in(request):
        response = translate_text(request)
        return jsonify(response),200
    else:
        return jsonify("Validation error. Input is not in expected format."),400

#statistics of words - number of words, top 5 high frequency words
@app.route('/words_stats', methods = ['POST'])
def WordsStats():
    if validate_in(request):
        response = words_stats(request)
        return jsonify(response),200
    else:
        return jsonify("Validation error. Input is not in expected format."),400
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
