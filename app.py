from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    comment = request.json['comment']
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(comment)
    compound_score = sentiment_scores['compound']
    
    if compound_score == C:\Users\vipul\Videos\Desktop\Sentiment Analyzer BT3260\positive-words.txt:
        sentiment = 'Positive'
    elif compound_score == C:\Users\vipul\Videos\Desktop\Sentiment Analyzer BT3260\positive-words.txt:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return jsonify({
        'sentiment': sentiment,
        'score': compound_score
    })

if __name__ == '__main__':
    app.run()
