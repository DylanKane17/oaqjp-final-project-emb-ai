import requests
import json

def emotion_detector(value):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = { "raw_document": { "text": value } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = obj, headers = headers)

    if response.status_code == 400:
        return {
        'anger': None,
        'fear': None,
        'joy': None,
        'disgust': None,
        'sadness': None,
        'dominant_emotion': None}
    
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]["emotion"]

    anger_score = emotion['anger']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    disgust_score = emotion['disgust']
    sadness_score = emotion['sadness']
    dominant_emotion = max(
        emotion.items(), key= lambda x: x[1]
        )[0]
    
    return {
        'anger': anger_score,
        'fear': fear_score,
        'joy': joy_score,
        'disgust': disgust_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
