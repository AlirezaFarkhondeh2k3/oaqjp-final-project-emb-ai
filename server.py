"""
Flask application for emotion detection.
Receives user input, sends it to the emotion detection API, and returns the detected emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('My Final Project')

@app.route('/emotionDetector')
def sent_emo():
    """
    Process user input and return the detected emotion.
    """
    text_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    out_put = f"""For the given statement, the system response is:
    'anger': {result['anger']}, 
    'disgust': {result['disgust']}, 
    'fear': {result['fear']}, 
    'joy': {result['joy']}, 
    'sadness': {result['sadness']}. 
    The dominant emotion is {result['dominant_emotion']}."""

    return out_put

@app.route('/')
def index_template():
    """
    Render the main page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
