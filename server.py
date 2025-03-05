"""
Flask Server for Emotion Detection API
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Handles emotion detection API.
    - Accepts a JSON request with 'text' key.
    - Returns the emotion analysis in JSON format.
    - If text is empty, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "No text provided for analysis.", 400

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    return f"For the given statement, the system response is 'anger': \
            {response['anger']}, 'disgust': {response['disgust']}, \
            'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': \
            {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """
    Renders the home page (index.html).
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
