## Summary:- 
This is a nlp based api in which user can perform basic text analytics operations. 

### Input:-
Json string which contains only one element. 
Key - 'text', Value - STRING

Sample input:- 

{
    "text": "Hope you’re doing awesome!"
    }


### Output:-
Response from api based on the selected api endpoint.

Sample output:- 

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

1. sentiment_analysis:-
Sentiment analysis - returns polarity and subjectivity in numbers and in text format.

2. correct_text:-
Correcting spelling of input text

3. detect_language:-
Language detection of input text

4. translate_text:-
Translate non-english language into english

5. words_stats:-
Statistics of words - returns number of words, top 5 high frequently used words
