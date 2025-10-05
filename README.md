# AI Pal & Parenting

🎯 **AI-powered emotional companion with privacy-first design**

A deployment-ready prototype that helps parents and young adults through an AI-powered system that respects user privacy. Features two main modes:

- **AI Pal (Teen/Young Adult)**: A private emotional companion using voice input and emotion analysis
- **AI Parenting Assistant (0–12 years)**: Coming soon features with elegant UI placeholders

## ✨ Features

### AI Pal Mode (Fully Functional)
- 🎤 **Voice Input**: Real-time speech-to-text using Web Speech API
- 🧠 **Emotion Analysis**: Detects Happy, Sad, Angry, Calm/Neutral emotions
- 🎨 **Visual Feedback**: Colored glowing rings for each emotion
- 🔒 **Privacy-First**: All processing happens locally, no cloud storage
- 📱 **Responsive Design**: Works on desktop and mobile

### Parent Assistant Mode (UI Preview)
- 🎯 Smart Parenting Suggestions
- 📊 Behavioral Insights  
- 📝 Daily Summary Reports
- 🔔 Child Safety Notifications

## 🛠️ Tech Stack

**Frontend:**
- Vanilla JavaScript with modern ES6+ features
- CSS3 with glassmorphism effects using backdrop-filter
- Web Speech API for voice recognition
- Responsive design with mobile support

**Backend:**
- FastAPI (Python) for high-performance API
- text2emotion library for emotion detection
- Fallback keyword-based emotion analysis
- CORS enabled for cross-origin requests

**Hosting:**
- Frontend: Can be deployed to Vercel, Netlify, or any static host
- Backend: Render, Railway, or Heroku compatible

## 🚀 Quick Start

### Frontend Setup

1. **Deploy the frontend** (already built and ready):
   ```bash
   # The frontend is already deployed and accessible
   # Or serve locally with any static server:
   python -m http.server 3000
   # or
   npx serve .
   ```

### Backend Setup

1. **Clone and setup backend**:
   ```bash
   mkdir ai-pal-backend
   cd ai-pal-backend

   # Copy the provided files: main.py, requirements.txt, Procfile
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**:
   ```bash
   python main.py
   # or
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Test the API**:
   ```bash
   curl -X POST "http://localhost:8000/analyze" \
        -H "Content-Type: application/json" \
        -d '{"text": "I am feeling great today!"}'
   ```

## 🌐 Deployment Instructions

### Frontend Deployment (Vercel)

1. **Upload files** to a new repository or use the provided HTML/CSS/JS files
2. **Connect to Vercel**:
   ```bash
   npm install -g vercel
   vercel --prod
   ```
3. **Update API endpoint** in the frontend code to point to your backend URL

### Backend Deployment (Render)

1. **Create a new Web Service** on [Render](https://render.com)
2. **Connect your repository** with the backend files
3. **Configure build settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host=0.0.0.0 --port=$PORT`
4. **Deploy** and copy the service URL

### Backend Deployment (Railway)

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```
2. **Deploy**:
   ```bash
   railway login
   railway init
   railway up
   ```

### Environment Configuration

Update the API endpoint in your frontend to match your deployed backend:
```javascript
// In app.js, change:
this.apiEndpoint = 'https://your-backend-url.com/analyze';
```

## 🔧 Configuration

### Emotion Detection
The system supports two emotion detection methods:

1. **text2emotion library** (preferred): Advanced NLP-based detection
2. **Keyword-based fallback**: Simple rule-based detection for reliability

### Privacy Settings
- **Local Processing**: All voice data is processed in the browser
- **No Data Storage**: No databases, cookies, or persistent storage
- **CORS Enabled**: Secure cross-origin requests
- **Session Only**: Data cleared on page reload

## 📚 API Documentation

### Endpoints

#### `POST /analyze`
Analyze emotion in text input.

**Request:**
```json
{
  "text": "I'm feeling amazing today!"
}
```

**Response:**
```json
{
  "emotion": "happy",
  "confidence": 0.85,
  "all_emotions": {
    "happy": 0.85,
    "sad": 0.05,
    "angry": 0.0,
    "fear": 0.0,
    "surprise": 0.1
  }
}
```

#### `GET /health`
Health check and system status.

**Response:**
```json
{
  "status": "healthy",
  "emotion_engine": "text2emotion",
  "privacy": "No data storage - fully local processing"
}
```

## 🎨 Design System

### Glassmorphism Effects
The UI uses modern glassmorphism with:
- Semi-transparent backgrounds (`backdrop-filter: blur()`)
- Subtle border highlights
- Gradient overlays (blue → purple → pink)
- Smooth animations and transitions

### Emotion Color Mapping
- **Happy**: Yellow glow (`#FFD700`)
- **Sad**: Blue glow (`#4FC3F7`)  
- **Angry**: Red glow (`#FF5252`)
- **Calm/Neutral**: Green glow (`#66BB6A`)

## 🔒 Privacy & Security

### Privacy Features
- ✅ **Local Processing**: Voice input processed in browser
- ✅ **No Cloud Storage**: Zero data persistence
- ✅ **No Tracking**: No analytics or user tracking
- ✅ **Secure Communication**: HTTPS-only in production
- ✅ **Transparent**: Clear privacy notices displayed

### Data Handling
- Voice input: Processed locally via Web Speech API
- Text analysis: Sent to backend for emotion detection only
- Results: Displayed immediately, not stored
- Session data: Cleared on page refresh

## 🐛 Troubleshooting

### Common Issues

1. **Voice Recognition Not Working**:
   - Ensure you're using Chrome/Edge (Firefox has limited support)
   - Allow microphone permissions
   - Use HTTPS in production

2. **Backend Connection Errors**:
   - Check CORS configuration
   - Verify API endpoint URL
   - Ensure backend is running and accessible

3. **Emotion Detection Errors**:
   - Backend will fallback to keyword-based detection
   - Check server logs for text2emotion installation issues

### Development Tips
- Use browser developer tools to monitor API calls
- Check console for JavaScript errors
- Test with different text inputs to verify emotion detection

## 🚦 Performance

### Frontend
- Lightweight vanilla JavaScript (~19KB)
- CSS3 animations using GPU acceleration
- Responsive design with mobile optimization

### Backend  
- FastAPI with high-performance async processing
- Text2emotion library with NLP optimization
- Fallback system for reliability

## 📄 License

This project is created for hackathon/prototype purposes. Feel free to use and modify as needed.

## 🤝 Contributing

This is a hackathon prototype. For production use, consider:

1. **Enhanced Security**: Add authentication, rate limiting
2. **Better Error Handling**: More comprehensive error states
3. **Advanced Emotion Detection**: Custom ML models, multi-language support
4. **Accessibility**: WCAG compliance, screen reader support
5. **Testing**: Unit tests, integration tests, end-to-end testing

---

## 📞 Support

For issues or questions about this prototype:
1. Check the troubleshooting section above
2. Review browser console for errors
3. Verify API endpoint configuration
4. Test with simple text inputs first

**Remember**: This is a privacy-focused application. All emotion analysis happens without storing personal data.
