from azure_translator import translate_to_english
from azure_sentiment  import analyze_sentiment

# Test 1: Finnish input
text_fi = "Tuote itsessään on todella laadukas ja toimii täsmälleen kuten kuvauksessa kerrottiin. Olen erittäin tyytyväinen ostokseen. Valitettavasti pakkaus oli pahasti vaurioitunut toimituksen aikana ja yksi tuotteen kulmista oli naarmuuntunut. Myös toimitus kesti huomattavasti odotettua kauemmin, lähes kaksi viikkoa. Asiakaspalvelu kuitenkin vastasi nopeasti reklamaatiooni, joten se oli positiivinen kokemus."
translation = translate_to_english(text_fi)
print("=== TRANSLATOR ===")
print(f"Detected language : {translation['detected_language']}")
print(f"Confidence        : {translation['confidence']}")
print(f"Translated        : {translation['translated_text']}")

# Test 2: Sentiment on the translated text
sentiment = analyze_sentiment(translation["translated_text"])
print("\n=== SENTIMENT ===")
print(f"Label    : {sentiment['label']}")
print(f"Positive : {sentiment['positive']:.0%}")
print(f"Neutral  : {sentiment['neutral']:.0%}")
print(f"Negative : {sentiment['negative']:.0%}")

print("\n=== ASPECTS ===")
for a in sentiment["aspects"]:
    print(f"{a['aspect']:<20} {a['sentiment']}")

# Test 3: Spanish input
text_es = "El producto es excelente, muy recomendado."
translation2 = translate_to_english(text_es)
sentiment2   = analyze_sentiment(translation2["translated_text"])
print("\n=== SPANISH TEST ===")
print(f"Detected   : {translation2['detected_language']}")
print(f"Translated : {translation2['translated_text']}")   # ← this line was missing
print(f"Label      : {sentiment2['label']}")
print(f"Positive   : {sentiment2['positive']:.0%}")