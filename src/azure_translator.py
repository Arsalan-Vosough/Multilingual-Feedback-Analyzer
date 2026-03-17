import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY    = os.getenv("AZURE_TRANSLATOR_KEY")
REGION = os.getenv("AZURE_TRANSLATOR_REGION")

def translate_to_english(text: str) -> dict:
    url     = "https://api.cognitive.microsofttranslator.com/translate"
    params  = {"api-version": "3.0", "to": "en"}
    headers = {
        "Ocp-Apim-Subscription-Key":    KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type":                 "application/json"
    }

    response = requests.post(url, params=params, headers=headers, json=[{"text": text}])
    response.raise_for_status()
    data = response.json()[0]

    return {
        "detected_language": data["detectedLanguage"]["language"],
        "confidence":        data["detectedLanguage"]["score"],
        "translated_text":   data["translations"][0]["text"]
    }