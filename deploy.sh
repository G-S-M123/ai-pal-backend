#!/bin/bash
# Simple deployment script for AI Pal & Parenting backend

echo "🚀 Deploying AI Pal & Parenting Backend..."

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found!"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "🎯 Starting FastAPI server..."
echo "🌐 Backend will be available at: http://localhost:8000"
echo "📚 API docs available at: http://localhost:8000/docs"
echo "🔒 Privacy: No data storage - fully local processing"

python main.py
