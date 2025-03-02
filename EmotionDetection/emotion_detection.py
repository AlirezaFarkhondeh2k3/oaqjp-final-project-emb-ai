import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function takes an image file as input and returns the emotion detected in the image.
    The emotion can be one of the following: 'happy', 'sad', 'neutral', 'surprise', 'fear', 'angry'.
    """

    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json=myobj, headers=header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    modify_response = json.loads(response.text)
    emotions = modify_response['emotionPredictions'][0]['emotion']
    max_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': max_emotion
    }
