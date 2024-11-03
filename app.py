import g4f
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import cv2
import threading
import random
from collections import Counter
from fer import FER  


engine = pyttsx3.init()


messages = [
    {"role": "system", "content": "Your name is MoodBot. You are designed to respond to users' queries and detect their mood."},
    {"role": "system", "content": "Provide fun responses based on user mood."},
]

fun_responses = {
    "happy": ["That's great to hear! Why don't you tell me a joke?", "I'm glad you're happy! Keep smiling! 😊"],
    "sad": ["I'm here for you! Want to talk about it?", "It's okay to feel sad sometimes. How can I cheer you up?"],
    "neutral": ["That's interesting! How about we chat about something fun?", "What else is on your mind?"],
}

detector = FER()

def GPT(message, mood):
    global messages
    messages.append({'role': 'user', 'content': f"{message} (mood: {mood})"})  

    providers = [
        g4f.Provider.HuggingChat,
        g4f.Provider.AmigoChat,
        g4f.Provider.ChatHub
    ]

    for provider in providers:
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                provider=provider,
                messages=messages
            )

            if isinstance(response, dict) and 'choices' in response:
                ms = response['choices'][0]['message']['content']
            else:
                ms = response or "   "

            messages.append({'role': 'assistant', 'content': ms})
            return ms
        except Exception as e:
            print(f"Error with provider {provider.__name__}: {e}")
            continue

    return "Sorry, something went wrong with all providers."

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        user_query = r.recognize_google(audio)
        print(f"User query: {user_query}")
        return user_query
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error with the API request: {e}")
        return None

def detect_mood():
    cap = cv2.VideoCapture(0)
    emotions_detected = []

    for _ in range(10):  
        ret, frame = cap.read()
        if ret:
            emotions = detector.detect_emotions(frame)
            if emotions:

                dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
                emotions_detected.append(dominant_emotion)
                print(f"Detected emotion: {dominant_emotion}")


        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


    if emotions_detected:
        most_common_emotion = Counter(emotions_detected).most_common(1)[0][0]
    else:
        most_common_emotion = "neutral"

    print(f"Most common detected emotion: {most_common_emotion}")
    return most_common_emotion

def handle_query(query):

    mood = detect_mood()


    response = GPT(query, mood)


    fun_response = random.choice(fun_responses.get(mood, ["I'm here for you!"]))
    

    speak(response)
    speak(fun_response)
    return response, fun_response

def send_query(query):
    if query.strip():
        response, fun_response = handle_query(query)
        
        
        response_box.configure(state=tk.NORMAL)
        response_box.insert(tk.END, f"You: {query}\n", 'user')
        response_box.insert(tk.END, f"MoodBot: {response}\n", 'bot')
        response_box.insert(tk.END, f"MoodBot (fun): {fun_response}\n\n", 'fun')
        response_box.configure(state=tk.DISABLED)
        response_box.see(tk.END)


def listen_thread():
    while True:
        user_query = listen()
        if user_query:
            send_query(user_query)


window = tk.Tk()
window.title("MoodBot")
window.geometry("450x700")
window.configure(bg="#2E3440")


style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), foreground="#D8DEE9", background="#5E81AC")
style.configure("TLabel", font=("Helvetica", 12), foreground="#ECEFF4", background="#2E3440")
style.configure("TEntry", font=("Helvetica", 12), foreground="#3B4252", padding=5)


title_label = ttk.Label(window, text="MoodBot", font=("Helvetica", 20, "bold"), background="#5E81AC", foreground="#ECEFF4")
title_label.pack(pady=10)


response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED, bg="#3B4252", fg="#D8DEE9", font=("Helvetica", 12))
response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
response_box.tag_config('user', foreground="#A3BE8C", font=("Helvetica", 12, "bold"))
response_box.tag_config('bot', foreground="#BF616A", font=("Helvetica", 12, "italic"))
response_box.tag_config('fun', foreground="#EBCB8B", font=("Helvetica", 12))


input_frame = ttk.Frame(window)
input_frame.pack(pady=5, fill=tk.X)
input_box = ttk.Entry(input_frame, width=50)
input_box.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)


send_button = ttk.Button(input_frame, text="Send", command=lambda: send_query(input_box.get()))
send_button.pack(side=tk.RIGHT, padx=5)


def quit_application():
    cv2.destroyAllWindows()  
    window.quit()


def stop_all():
    cv2.destroyAllWindows()
    window.quit() 


stop_button = ttk.Button(window, text="Stop All", command=stop_all)
stop_button.pack(pady=10)


window.bind('<q>', lambda event: quit_application())


def on_enter(event):
    send_query(input_box.get())
    input_box.delete(0, tk.END)  


input_box.bind('<Return>', on_enter)


threading.Thread(target=listen_thread, daemon=True).start()

window.mainloop()

