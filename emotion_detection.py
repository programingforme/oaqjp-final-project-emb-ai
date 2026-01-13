import json
import requests

def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=input_text, timeout=10)
    json_response = json.loads(response.text)

    anger = json_response['emotionPredictions'][0]['emotion']['anger']
    disgust = json_response['emotionPredictions'][0]['emotion']['disgust']
    fear = json_response['emotionPredictions'][0]['emotion']['fear']
    joy = json_response['emotionPredictions'][0]['emotion']['joy']
    sadness = json_response['emotionPredictions'][0]['emotion']['sadness']
    
    result =  {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion

    return result
    