import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import (
    Features, KeywordsOptions, CategoriesOptions, SentimentOptions
)
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator(os.getenv("IBM_API_KEY"))
nlu = NaturalLanguageUnderstandingV1(
    version="2022-04-07",
    authenticator=authenticator
)
nlu.set_service_url(os.getenv("IBM_URL"))

def analyze_text(text: str) -> dict:
    response = nlu.analyze(
        text=text,
        features=Features(
            keywords=KeywordsOptions(limit=5),
            categories=CategoriesOptions(limit=3)
        )
    ).get_result()

    keywords = [
        {
            "text":      k["text"],
            "relevance": round(k["relevance"], 2)
        }
        for k in response.get("keywords", [])
    ]

    categories = list(dict.fromkeys([
        c["label"].strip("/").replace("/", " > ")
        for c in response.get("categories", [])
    ]))

    return {
        "keywords":   keywords,
        "categories": categories
    }