import requests
import json


def emotion_detector(text_to_analyze):
    DEFAULT_RES = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not text_to_analyze.strip():
        return DEFAULT_RES

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return DEFAULT_RES

    result = response.json()
    emotions = result.get("emotionPredictions", [{}])[0]
    emotion = emotions.get("emotion", {})

    print(emotion)

    emotion_scores = {
        "anger": emotion.get("anger", 0),
        "disgust": emotion.get("disgust", 0),
        "fear": emotion.get("fear", 0),
        "joy": emotion.get("joy", 0),
        "sadness": emotion.get("sadness", 0),
    }

    emotion_scores["dominant_emotion"] = max(emotion_scores, key=emotion_scores.get)
    return emotion_scores
