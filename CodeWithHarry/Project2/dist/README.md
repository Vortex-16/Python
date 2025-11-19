# Alpha Voice Assistant - Deployment Package

This folder contains the standalone executable for the Alpha Voice Assistant.

## Contents:
- `Alpha-Assistant.exe` - The main executable
- `.env` - Environment variables file (configure your API keys here)
- `musicLibrary.py` - Music library configuration
- `README.md` - This file

## Setup Instructions:

### 1. Configure API Keys
Edit the `.env` file and add your actual API keys:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
NEWS_API_KEY=your_actual_news_api_key_here
```

### 2. Get API Keys:
- **Gemini API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **News API Key**: Visit [NewsAPI.org](https://newsapi.org/) (free tier available)

### 3. Run the Application
Simply double-click `Alpha-Assistant.exe` or run it from command line.

## Usage:
1. Say "Alpha" to activate the assistant
2. Wait for the confirmation sound
3. Give your command
4. Available commands:
   - "Open Google/Facebook/YouTube/LinkedIn"
   - "Play [song name]" (from musicLibrary.py)
   - "News" - Get latest headlines
   - Any question - Will be answered by AI

## Troubleshooting:
- Make sure your microphone is working and permissions are granted
- Ensure API keys are correctly set in the `.env` file
- For firewall issues, allow the executable through Windows Firewall
- If speech recognition doesn't work, try speaking closer to the microphone

## System Requirements:
- Windows 10 or later
- Working microphone
- Internet connection
- Minimum 4GB RAM recommended
