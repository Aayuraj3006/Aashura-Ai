# 🤖 Aashura AI — Your Personal Desktop Voice Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Eel-Framework-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

> **Aashura AI** is a smart and customizable desktop assistant built using **Python**, **Eel**, **HTML/CSS**, and **JavaScript**. Control your PC and mobile with simple voice or typed commands — from launching apps to making calls and chatting, Aashura AI brings AI and automation right to your fingertips.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ Voice & Typing Control | Interact using your voice or keyboard |
| 📞 Phone Calls via Mobile | Make calls through your Android device |
| 📲 Call Management | Pick up and disconnect calls remotely |
| 💻 App Launcher | Launch desktop applications instantly |
| 🌐 URL Opener | Open your favorite websites with a command |
| 📔 Phone Book | Built-in contact management system |
| 🙋 Personal Details | Store and use your personal profile |
| 🤖 Chat Interaction | Conversational AI chat support |
| 🎵 Media Control | Play videos/songs on YouTube & Spotify |
| 🌤️ Weather Updates | Get real-time weather information |

---

## 🛠️ Tech Stack

- **Backend:** Python 3.8+
- **Bridge:** [Eel](https://github.com/python-eel/Eel) (Python ↔ JavaScript communication)
- **Frontend:** HTML5, CSS3, JavaScript
- **Voice Recognition:** SpeechRecognition / Web Speech API
- **Android Bridge:** ADB (Android Debug Bridge) for mobile call control

---

## 📁 Project Structure

```
aashura-ai/
│
├── main.py                 # Entry point — starts the Eel app
├── config.py               # User settings & personal details
├── phonebook.json          # Stored contacts
│
├── features/
│   ├── voice.py            # Voice recognition & TTS
│   ├── calls.py            # Mobile call control via ADB
│   ├── apps.py             # Desktop app launcher
│   ├── browser.py          # URL opener
│   ├── media.py            # YouTube & Spotify control
│   ├── weather.py          # Weather API integration
│   └── chat.py             # AI chat interaction
│
└── web/
    ├── index.html          # Main UI
    ├── style.css           # Styling
    └── script.js           # Frontend logic & Eel calls
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- Node.js (optional, for frontend tooling)
- Android Debug Bridge (ADB) — for mobile call features
- Android device with USB Debugging enabled (for call features)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/aashura-ai.git
cd aashura-ai
```

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure your details**

Edit `config.py` or the settings panel in the app to add:
- Your name and personal details
- API keys (Weather API, etc.)
- Default apps and URLs

**4. Run Aashura AI**

```bash
python main.py
```

---

## 📱 Mobile Call Setup (Android)

To enable phone call features, connect your Android device via USB and enable USB Debugging:

1. On your Android device, go to **Settings → About Phone** and tap **Build Number** 7 times to unlock Developer Options.
2. Go to **Settings → Developer Options** and enable **USB Debugging**.
3. Connect your device via USB and run:

```bash
adb devices
```

4. Confirm your device appears in the list. Aashura AI will now be able to make, pick up, and disconnect calls through your mobile.

---

## 🎙️ Voice Commands — Quick Reference

| Command | Action |
|---|---|
| `"Open YouTube"` | Launches YouTube in browser |
| `"Call [Name]"` | Dials contact from phone book |
| `"Pick up the call"` | Answers incoming call |
| `"Disconnect the call"` | Ends active call |
| `"Open [App Name]"` | Launches desktop application |
| `"Play [Song] on Spotify"` | Plays song on Spotify |
| `"What's the weather today?"` | Fetches current weather |
| `"My name is..."` | Saves personal detail |

---

## ⚙️ Configuration

All user preferences can be set inside `config.py`:

```python
USER_NAME = "Your Name"
CITY = "Your City"            # Used for weather
WEATHER_API_KEY = "your_key"  # OpenWeatherMap API key
DEFAULT_BROWSER = "chrome"
```

Contacts are stored in `phonebook.json`:

```json
{
  "Mom": "+91XXXXXXXXXX",
  "Office": "+91XXXXXXXXXX"
}
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

Please make sure your code follows the existing style and includes comments where appropriate.

---

## 🐛 Known Issues & Roadmap

- [ ] iOS support (currently Android only for calls)
- [ ] Wake word detection ("Hey Aashura")
- [ ] Plugin system for custom commands
- [ ] Multi-language voice support
- [ ] Smart home device integration

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Eel](https://github.com/python-eel/Eel) — Python/JS desktop app framework
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — Voice input library
- [OpenWeatherMap](https://openweathermap.org/api) — Weather data API
- [ADB (Android Debug Bridge)](https://developer.android.com/studio/command-line/adb) — Android call control

---

<p align="center">Made with ❤️ by the Aashura AI Team</p>
