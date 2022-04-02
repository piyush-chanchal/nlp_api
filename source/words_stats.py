import json
from textblob import TextBlob
from collections import Counter

def words_stats(request):
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    in_text = in_nlp['text']

    out_wcounts = len(TextBlob(in_text).words)
    
    split_text = TextBlob(in_text).split()
    words_freq = Counter(split_text)
    
    most_occur = words_freq.most_common(5)

    response = {"Word Counts": out_wcounts, "Top 5 most frequent words": most_occur}
    return response