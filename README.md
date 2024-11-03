
MoodBot is a fun and innovative AI companion I developed for the Useless Projects Make-a-thon, organized by TinkerHub Campus Chapter. The hackathon challenged participants to create projects with a twist of humor and creativity, and that’s how MoodBot was born! It’s an AI-powered bot that not only chats but also detects your mood through facial expressions, offering witty and mood-based responses to brighten your day.

# MoodBot: Your Hilarious AI Companion 🤖🎭

**MoodBot** is an AI-powered virtual companion that understands your mood through facial expression analysis and responds in fun, mood-appropriate ways! Engage with MoodBot through voice or text, and get ready for mood-based humor and witty conversations, designed to put a smile on your face!

---

## 🌟 Key Features
- **Voice & Text Interaction**: Chat seamlessly with MoodBot, whether you prefer typing or speaking.
- **Emotion Recognition**: MoodBot uses real-time facial expression analysis to understand your emotions and tailor responses that match your mood.
- **AI-Powered Conversations**: Integrates GPT-based responses to provide engaging and creative answers to your queries.
- **Mood-Based Humor**: Depending on your mood, MoodBot cracks jokes, offers motivational support, or delivers uplifting messages.
- **Interactive & Beautiful UI**: A sleek, modern interface for a delightful user experience.

---

## 🤖 How MoodBot Works
1. **Facial Emotion Detection**: Using the `FER` library, MoodBot captures live webcam feed and analyzes your facial expressions to detect your current mood, such as happy, sad, or neutral.
2. **Voice Recognition**: Powered by `speech_recognition`, MoodBot listens to your voice and understands what you’re saying, just like a personal assistant.
3. **Intelligent Responses**: Using the `g4f` library, MoodBot generates GPT-based replies, making each conversation feel human-like and engaging.
4. **Humorous Reactions**: Based on your detected mood, MoodBot lightens the atmosphere with jokes, motivational talks, or empathetic messages.

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.7 or higher** is required to run this project.
- A webcam and microphone for full functionality.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MoodBot.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd MoodBot
   ```
3. **Set Up a Virtual Environment**:
   ```bash
   python -m venv moodbot_env
   moodbot_env\Scripts\activate  # Windows
   source moodbot_env/bin/activate  # MacOS/Linux
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Application**:
   ```bash
   python app.py
   ```

---

## 📸 Screenshots
> *Showcasing MoodBot in action!*

![Main Interface](https://github.com/Ziyad765/MoodBot/blob/main/Samples/UI%201.png)
![User Interface](https://github.com/Ziyad765/MoodBot/blob/main/Samples/Interface.png)
![User Interface](https://github.com/Ziyad765/MoodBot/blob/main/Samples/UI%202.png)
![Emotion Detection](https://github.com/Ziyad765/MoodBot/blob/main/Samples/face%20detection%201.png)
![Emotion Detection](https://github.com/Ziyad765/MoodBot/blob/main/Samples/face%20detection%202.png)

---

## 🛠 Technologies & Libraries
- **Python**: The core programming language for this project.
- **Tkinter**: Used for creating a user-friendly graphical interface.
- **FER**: Facial Emotion Recognition for detecting and analyzing facial expressions.
- **SpeechRecognition & Pyttsx3**: For speech input and output capabilities.
- **OpenCV**: Used for accessing the webcam and image processing.
- **g4f**: For generating dynamic and engaging AI responses.

---

## 🎨 UI Design
The MoodBot interface has been carefully crafted to provide:
- **A clean and minimalist design** that’s both functional and aesthetically pleasing.
- **Live Webcam Feed**: Embedded in the UI for seamless mood detection.
- **Scrollable Response Area**: View all past interactions in a neat and organized manner.
- **Interactive Elements**: Simple buttons and intuitive input boxes for easy use.

## 📚 Future Enhancements
- **Emotion-based Voice Modulation**: Making MoodBot’s voice output vary based on the detected emotion.
- **Improved AI Models**: Integrating more sophisticated models for even better emotion detection and response generation.
- **Customizable Avatars**: Adding visual avatars that change expressions based on user mood.
