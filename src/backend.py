from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from azure_translator import translate_to_english
from azure_sentiment import analyze_sentiment
from ibm_watson_nlu import analyze_text

app = FastAPI()

# Allow the React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

# ── /translate ─────────────────────────────────────────────
@app.post("/translate")
def translate(body: TextInput):
    result = translate_to_english(body.text)
    return {
        "translated_text":   result["translated_text"],
        "detected_language": result["detected_language"],
        "confidence":        result["confidence"]
    }

# ── /sentiment ─────────────────────────────────────────────
@app.post("/sentiment")
def sentiment(body: TextInput):
    translation = translate_to_english(body.text)
    result = analyze_sentiment(translation["translated_text"])
    return {
        "translated_text": translation["translated_text"],
        "sentiment":       result["label"],
        "score":           round(max(result["positive"], result["negative"]), 2),
        "positive":        result["positive"],
        "neutral":         result["neutral"],
        "negative":        result["negative"],
        "aspects":         result["aspects"]
    }

# ── /classify ──────────────────────────────────────────────
@app.post("/classify")
def classify(body: TextInput):
    # IBM Watson NLU goes here (next step)
    # returning placeholder for now so the UI doesn't break
    translation = translate_to_english(body.text)
    return {
        "translated_text": translation["translated_text"],
        "categories":      ["pending — IBM Watson not connected yet"],
        "keywords":        []
    }

# ── /pipeline ──────────────────────────────────────────────
@app.post("/classify")
def classify(body: TextInput):
    translation = translate_to_english(body.text)
    watson      = analyze_text(translation["translated_text"])
    return {
        "translated_text": translation["translated_text"],
        "categories":      watson["categories"],
        "keywords":        [k["text"] for k in watson["keywords"]]
    }

@app.post("/pipeline")
def pipeline(body: TextInput):
    translation = translate_to_english(body.text)
    translated  = translation["translated_text"]
    sentiment   = analyze_sentiment(translated)
    watson      = analyze_text(translated)

    return {
        "translated_text":   translated,
        "detected_language": translation["detected_language"],
        "sentiment":         sentiment["label"],
        "score":             round(max(sentiment["positive"], sentiment["negative"]), 2),
        "positive":          sentiment["positive"],
        "neutral":           sentiment["neutral"],
        "negative":          sentiment["negative"],
        "aspects":           sentiment["aspects"],
        "categories":        watson["categories"],
        "keywords":          [k["text"] for k in watson["keywords"]]
    }