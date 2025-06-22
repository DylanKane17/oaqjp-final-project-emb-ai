"""Module providing a server to run Emotion Detection."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Function rendering index page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=["GET"])
def detect_emotion():
    """Function that handles emotion detecting."""
    value = request.args.get('textToAnalyze')

    result = emotion_detector(value)

    if  result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is '{dominant_emotion}'."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(debug="True")
