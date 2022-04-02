## Summary:- 
This is a nlp based api in which user can perform basic text analytics operations. 

### Input:-
Json string which contains only one element. 
Key - 'text', Value - STRING

<b>Sample input:- </b>

{
    "text": "Hope you’re doing awesome!"
    }


### Output:-
Response from api based on the selected api endpoint.

<b>Sample output:- </b>

{
    "Number Response": {
        "Sentiment": 1.0,
        "Subjectivity": 1.0
    },
    "Text Response": {
        "Sentiment": "Positive",
        "Subjectivity": "High"
    }
}


### API Endpoints:-

<b>1. sentiment_analysis:-</b>
Sentiment analysis - returns polarity and subjectivity in numbers and in text format.

<b>2. correct_text:-</b>
Correcting spelling of input text

<b>3. detect_language:-</b>
Language detection of input text

<b>4. translate_text:-</b>
Translate non-english language into english

<b>5. words_stats:-</b>
Statistics of words - returns number of words, top 5 high frequently used words
