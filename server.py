''' This is the final project
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion_Detection')

@app.route('/emotionDetector')
def emotion_detection():
    ''' The emotion_detection endpoint
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion:
        return_response = f"For the given statement, the system response is 'anger': {anger}, " \
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " \
        f"The dominant emotion is {dominant_emotion}."
    else:
        return_response = "Invalid text! Please try again!"

    return return_response


@app.route("/")
def index_page():
    ''' The index_page endpoint
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
