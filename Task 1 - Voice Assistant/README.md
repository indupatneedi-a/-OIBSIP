#`OIBSP/PYTHON-TASK1-VOICEASSISTANT/`
# 🎙️ Voice Assistant
> **Oasis Infobyte Summer Internship Program (OIBSIP)**
> **Track:** Python Programming | **Task 1:** Voice Assistant | **Tier:** Beginner

A simple Python voice assistant that listens to spoken commands through the microphone and replies by voice and text. It can greet you, tell the time and date, and search the web for any topic you say.
## 📌 Features

- 🎤 Captures voice input from the microphone using `speech_recognition`
- 👋 Responds to "hello", "hi", or "hey" with a greeting
- 🕒 Tells the current **time** on request
- 📅 Tells today's **date** on request
- 🔎 Performs a **web search**: say "search for python tutorials" and the browser opens with the results
- 🔊 Speaks every response aloud using `pyttsx3` (text-to-speech) and also prints it
- ⚠️ Graceful error handling: asks you to repeat if speech isn't understood, and warns if there is no internet connection
- 👋 Exits cleanly when you say "exit", "stop", "bye", or "quit"

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Programming language |
| `speech_recognition` | Converts speech to text |
| `pyttsx3` | Converts text to speech (works offline) |
| `PyAudio` | Gives Python access to the microphone |
| `datetime` | Gets the current time and date (built in) |
| `webbrowser` | Opens the browser for web searches (built in) |
| `urllib.parse` | Makes search text safe for URLs (built in) |

---

## 📂 Project Structure

```
Python-Task1-VoiceAssistant/
│
├── voice_assistant.py     # Main source code
├── README.md              # Project documentation
└── screenshots/           # Output screenshots
---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/[your-github-username]/OIBSIP.git
cd OIBSIP/Python-Task1-VoiceAssistant
```

### 2. Install the required libraries
```bash
pip install pyttsx3 SpeechRecognition pyaudio
```

### 3. If PyAudio fails to install

| Operating System | Fix |
|---|---|
| **Windows** | Run `python -m pip install --upgrade pip`, then retry. If it still fails: `pip install pipwin` and then `pipwin install pyaudio` |
| **macOS** | `brew install portaudio` then `pip install pyaudio` |
| **Linux** | `sudo apt install portaudio19-dev espeak` then `pip install pyaudio` |

### Requirements
- A working **microphone**
- An **internet connection** (needed for speech recognition)

---

## ▶️ How to Run

```bash
python voice_assistant.py
```

In a **Jupyter Notebook**, install the libraries with `!pip install pyttsx3 SpeechRecognition pyaudio`, then run the code in a cell.

---

## 🗣️ Example Commands

| You say | Assistant does |
|---|---|
| "Hello" | Replies "Hello! How can I help you today?" |
| "What is the time?" | Speaks the current time, e.g. "The time is 03:45 PM" |
| "What is the date today?" | Speaks the date, e.g. "Today is Monday, 23 November 2026" |
| "Search for Python tutorials" | Opens Google with results for "Python tutorials" |
| "Bye" / "Exit" / "Stop" | Says goodbye and quits |

---

## 🧠 How It Works

1. **`speak(text)`** prints the text and says it aloud using `pyttsx3`.
2. **`listen()`** records audio from the microphone, adjusts for background noise, and sends the audio to Google's speech recognition service. It returns the text in lowercase.
3. **`handle_command(command)`** checks the text for keywords (hello, time, date, search, exit) and performs the matching action. It returns `False` when the user wants to quit.
4. **`main()`** runs a loop: listen → handle command → repeat until the user says "bye".

---

## 🛡️ Error Handling

| Situation | What the assistant does |
|---|---|
| No speech detected (timeout) | Returns silently and listens again |
| Speech not understood | Says "Sorry, I did not understand that. Please repeat." |
| No internet / service unreachable | Says to check the internet connection |
| Empty search query | Asks "What would you like me to search for?" |
| Unknown command | Lists what the assistant can do |

---

## 🔒 Privacy Note

- Your voice is captured **only while the program is running** and the "Listening..." message is shown.
- Audio is sent to **Google's free Web Speech API** (through `recognize_google`) to be converted to text, so an internet connection is required. See Google's privacy policy for how they handle this data.
- Text-to-speech runs **locally** on your computer.
- This program does **not** save any audio or text to files.

---
## Screenshots
<img width="1920" height="816" alt="1000095994" src="https://github.com/user-attachments/assets/6d348616-2972-4940-8f74-c18551b7cd36" />

<img width="1920" height="816" alt="1000095993" src="https://github.com/user-attachments/assets/d9852083-13d5-49ef-b1ec-2591567b394a" />

## 🎥 Demo Video
🔗https://lnkd.in/p/d_wgvrSm

## ⚠️ Known Limitations
- Uses **keyword matching**, not full natural language understanding, so unusual phrasing may not be recognised.
- Short keywords like "hi" can match inside other words (for example "this"). This could be improved by splitting the sentence into words before checking.
- Speech recognition accuracy depends on the microphone quality, accent, and background noise.

## 🚀 Future Improvements

- Natural language understanding to parse free-form sentences
- Voice-controlled email using `smtplib`
- Timed reminders with audible alerts
- Live weather updates through the OpenWeatherMap API
- Support for custom commands through a config file

## 🙏 Acknowledgements

Thanks to **Oasis Infobyte** for the internship opportunity.

`#oasisinfobyte` `#python` `#internship` `#voiceassistant`
