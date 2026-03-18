# Multilingual Feedback Analyzer

A smart web application that analyzes customer feedback written in any language. It automatically translates the text to English, runs sentiment analysis, and extracts keywords and categories — all powered by Microsoft Azure and IBM Watson cognitive services.

---

## What it does

1. **Translates** customer reviews from any language to English (Azure Translator)
2. **Analyzes sentiment** — overall score + aspect-level breakdown per topic (Azure Text Analytics)
3. **Extracts keywords and categories** — what the review is about (IBM Watson NLU)
4. **Runs the full pipeline** in one click — all three steps at once

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + Tailwind CSS |
| Backend | Python + FastAPI |
| Translation | Microsoft Azure Translator API |
| Sentiment | Microsoft Azure Text Analytics (Language service) |
| Keywords | IBM Watson Natural Language Understanding |

---

## Project structure

```
Multilingual-Feedback-Analyzer/
├── src/
│   ├── azure_translator.py   # Azure Translator API integration
│   ├── azure_sentiment.py    # Azure Text Analytics integration
│   ├── ibm_watson_nlu.py     # IBM Watson NLU integration
│   ├── backend.py            # FastAPI backend (routes)
│   ├── App.jsx               # React frontend
│   ├── main.jsx              # React entry point
│   ├── index.css             # Tailwind styles
│   └── test_azure.py         # Test script for Azure services
├── index.html
├── .env                      # API keys 
├── .gitignore
├── package.json
└── README.md
```

---

## Setup instructions

### 1. Clone the repo

```bash
git clone https://github.com/Arsalan-Vosough/Multilingual-Feedback-Analyzer.git
cd Multilingual-Feedback-Analyzer
```

### 2. Create your `.env` file

Create a file called `.env` in the project root — **never commit this file**:

```
AZURE_TRANSLATOR_KEY=your_azure_translator_key
AZURE_TRANSLATOR_REGION=northeurope

AZURE_LANGUAGE_KEY=your_azure_language_key
AZURE_LANGUAGE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/

IBM_API_KEY=your_ibm_watson_api_key
IBM_URL=https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id
```

### 3. Get your API keys

**Microsoft Azure (Translator + Language service):**
1. Go to [portal.azure.com](https://portal.azure.com) and create a free account
2. Create a **Translator** resource (Free F0 tier) → copy Key 1 + Region
3. Create a **Language** resource (Free F0 tier) → copy Key 1 + Endpoint URL

**IBM Watson NLU:**
1. Go to [cloud.ibm.com](https://cloud.ibm.com) and create a free account
2. Create a **Natural Language Understanding** service (Lite tier)
3. Copy API key + Service URL

### 4. Install Python dependencies

```bash
cd src
pip install fastapi uvicorn requests python-dotenv ibm-watson
```

### 5. Install frontend dependencies

```bash
cd ..
npm install
```

---

## Running the app

You need **two terminals open at the same time**:

**Terminal 1 — start the backend:**
```bash
cd src
uvicorn backend:app --reload --port 8000
```

You should see:
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Terminal 2 — start the frontend:**
```bash
npm run dev
```

Then open your browser at **http://localhost:5173**

---

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/translate` | Detect language + translate to English |
| POST | `/sentiment` | Sentiment analysis + aspect-level opinions |
| POST | `/classify` | Keywords + categories via IBM Watson |
| POST | `/pipeline` | Run all three steps at once |

All endpoints accept:
```json
{ "text": "your review text in any language" }
```

---

## Example output

Input (Finnish):
> "Tuote itsessään on todella laadukas. Valitettavasti pakkaus oli pahasti vaurioitunut toimituksen aikana."

Output:
```json
{
  "translated_text": "The product itself is really high quality. Unfortunately the packaging was badly damaged during delivery.",
  "detected_language": "fi",
  "sentiment": "mixed",
  "positive": 0.60,
  "neutral": 0.01,
  "negative": 0.40,
  "aspects": [
    { "aspect": "product", "sentiment": "positive" },
    { "aspect": "packaging", "sentiment": "negative" },
    { "aspect": "delivery", "sentiment": "negative" }
  ],
  "keywords": ["packaging", "delivery", "product quality"],
  "categories": ["Shopping/E-commerce", "Customer service"]
}
```


---

## Group members

| Name | Contribution |
|---|---|
| Arsalan Vosough | Azure Translator + Azure Text Analytics + IBM Watson NLU integration + FastAPI backend |
| Declen |  |
| Haben Eyasu | React frontend |

---

