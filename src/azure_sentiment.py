import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY      = os.getenv("AZURE_LANGUAGE_KEY")
ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")

def analyze_sentiment(text: str) -> dict:
    url     = ENDPOINT + "language/:analyze-text?api-version=2023-04-01"
    headers = {
        "Ocp-Apim-Subscription-Key": KEY,
        "Content-Type":              "application/json"
    }
    body = {
        "kind": "SentimentAnalysis",
        "parameters": {
            "modelVersion":  "latest",
            "opinionMining": True
        },
        "analysisInput": {
            "documents": [{"id": "1", "language": "en", "text": text}]
        }
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    doc = response.json()["results"]["documents"][0]

    result = {
        "label":    doc["sentiment"],
        "positive": doc["confidenceScores"]["positive"],
        "neutral":  doc["confidenceScores"]["neutral"],
        "negative": doc["confidenceScores"]["negative"],
        "aspects":  []
    }

    for sentence in doc["sentences"]:
        for assessment in sentence.get("targets", []):
            result["aspects"].append({
                "aspect":    assessment["text"],
                "sentiment": assessment["sentiment"],
                "positive":  assessment["confidenceScores"]["positive"],
                "negative":  assessment["confidenceScores"]["negative"]
            })

    return result