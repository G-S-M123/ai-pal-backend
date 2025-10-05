
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import Dict
import re

# Try to import text2emotion, fallback to simple keyword detection
try:
    import text2emotion as te
    USE_TEXT2EMOTION = True
except ImportError:
    USE_TEXT2EMOTION = False
    print("text2emotion not available, using keyword-based emotion detection")

app = FastAPI(
    title="AI Pal & Parenting API",
    description="Privacy-focused emotion analysis API for AI Pal & Parenting application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotion: str
    confidence: float
    all_emotions: Dict[str, float]

# Simple keyword-based emotion detection as fallback
def keyword_based_emotion_detection(text: str) -> Dict[str, float]:
    """
    Simple keyword-based emotion detection using predefined word lists
    """
    text_lower = text.lower()

    # Emotion keywords
    emotion_keywords = {
        'happy': ['happy', 'joy', 'excited', 'great', 'amazing', 'wonderful', 'fantastic', 
                  'awesome', 'good', 'love', 'smile', 'laugh', 'cheerful', 'delighted'],
        'sad': ['sad', 'depressed', 'unhappy', 'miserable', 'upset', 'down', 'blue', 
                'grief', 'sorrow', 'cry', 'tears', 'lonely', 'heartbroken'],
        'angry': ['angry', 'mad', 'furious', 'rage', 'hate', 'annoyed', 'frustrated', 
                  'irritated', 'pissed', 'outraged', 'livid', 'enraged'],
        'fear': ['afraid', 'scared', 'fear', 'terrified', 'worried', 'anxious', 'panic', 
                 'nervous', 'frightened', 'alarmed', 'concerned'],
        'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'stunned', 
                     'bewildered', 'confused', 'wow', 'unbelievable']
    }

    scores = {emotion: 0.0 for emotion in emotion_keywords.keys()}
    total_words = len(text.split())

    if total_words == 0:
        return scores

    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            # Count occurrences of each keyword
            count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text_lower))
            scores[emotion] += count

    # Normalize scores
    max_score = max(scores.values()) if any(scores.values()) else 1
    if max_score > 0:
        scores = {k: v / max_score for k, v in scores.items()}

    # If no emotions detected, return neutral (calm)
    if all(score == 0 for score in scores.values()):
        scores['happy'] = 0.1  # Very low baseline

    return scores

def analyze_emotion_text2emotion(text: str) -> Dict[str, float]:
    """
    Analyze emotion using text2emotion library
    """
    try:
        emotions = te.get_emotion(text)
        # text2emotion returns: Happy, Angry, Sad, Surprise, Fear
        # Map to our expected format
        emotion_mapping = {
            'Happy': 'happy',
            'Angry': 'angry', 
            'Sad': 'sad',
            'Surprise': 'surprise',
            'Fear': 'fear'
        }

        mapped_emotions = {}
        for original, mapped in emotion_mapping.items():
            mapped_emotions[mapped] = emotions.get(original, 0.0)

        return mapped_emotions
    except Exception as e:
        print(f"Error with text2emotion: {e}")
        return keyword_based_emotion_detection(text)

def get_dominant_emotion(emotions: Dict[str, float]) -> tuple:
    """
    Get the dominant emotion and its confidence score
    """
    if not emotions or all(score == 0 for score in emotions.values()):
        return 'neutral', 0.0

    max_emotion = max(emotions.items(), key=lambda x: x[1])
    emotion, confidence = max_emotion

    # If confidence is very low, classify as neutral/calm
    if confidence < 0.1:
        return 'calm', confidence

    return emotion, confidence

@app.get("/")
async def root():
    return {
        "message": "AI Pal & Parenting API",
        "status": "active",
        "privacy": "All data processed locally - no storage",
        "endpoints": {
            "/analyze": "POST - Analyze text emotion",
            "/health": "GET - Health check"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "emotion_engine": "text2emotion" if USE_TEXT2EMOTION else "keyword-based",
        "privacy": "No data storage - fully local processing"
    }

@app.post("/analyze", response_model=EmotionResponse)
async def analyze_emotion(input_data: TextInput):
    """
    Analyze emotion in the provided text.
    Returns the dominant emotion with confidence score.
    """
    try:
        text = input_data.text.strip()

        if not text:
            raise HTTPException(status_code=400, detail="Text input cannot be empty")

        if len(text) > 1000:
            raise HTTPException(status_code=400, detail="Text too long (max 1000 characters)")

        # Analyze emotion
        if USE_TEXT2EMOTION:
            emotions = analyze_emotion_text2emotion(text)
        else:
            emotions = keyword_based_emotion_detection(text)

        # Get dominant emotion
        dominant_emotion, confidence = get_dominant_emotion(emotions)

        return EmotionResponse(
            emotion=dominant_emotion,
            confidence=round(confidence, 3),
            all_emotions={k: round(v, 3) for k, v in emotions.items()}
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"Error analyzing emotion: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during emotion analysis")

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )
