**# Pyra - Your Virtual Assistant**

**## Overview**
Pyra is a Python-based virtual assistant designed to perform various tasks such as speech recognition, text-to-speech conversion, web searching, opening applications, and retrieving time and date information. It is built using Python's `speech_recognition`, `pyttsx3`, and `wikipedia` modules.

## Features
- Speech Recognition: Listens and processes voice commands using `speech_recognition`.
- Text-to-Speech (TTS): Converts text responses to speech using `pyttsx3`.
- Wikipedia Search: Retrieves short summaries from Wikipedia.
- Web Search: Opens a browser and searches Google.
- Application Launcher: Opens Notepad and plays music.
- Time & Date Retrieval: Provides the current time and date.
- Conversational Responses: Greets the user based on the time of day.

**## Installation**
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/pyra-voice-assistant.git
cd pyra-voice-assistant
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Step 3: Install Dependencies
Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt
```
#### If you face issues with `pyaudio`, install it manually:
```bash
pip install pipwin
pipwin install pyaudio
```

## Usage
Run the assistant using:
```bash
python Assist.py
```
After starting, Pyra will greet you and wait for your voice commands.

### Voice Commands Supported
- **Wikipedia Search**: _"Wikipedia Elon Musk"_
- **Web Search:** _"Search for Python tutorials"_
- **Open Notepad:** _"Open Notepad"_
- **Play Music**: _"Play music"_
- **Tell Time**: _"What is the time?"_
- **Tell Date**: _"What is the date today?"_
- **Exit:**_"Close the program"_

## Dependencies
- `speech_recognition` - For voice recognition
- `pyttsx3` - For text-to-speech
- `wikipedia` - For Wikipedia searches
- `webbrowser` - To open search results
- `os` - To open system applications
- `datetime` - To fetch time and date

## Troubleshooting
- PyAudio Not Found:
  - Install manually using pipwin: `pip install pipwin && pipwin install pyaudio`
- Microphone Not Working:
  - Ensure your microphone is set as the default recording device.
  - Try running `python -m speech_recognition` to debug.

## Author
Amar Ranjan Panda
