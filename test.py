# # # import g4f
# # # import re
# # # from head.listen import take_command
# # # from head.speak import speak

# # # messages = [
# # #     {"role": "system", "content": "your name is eniac and you are developed by computer science and design engineering students of government engineering college kozhikode"},
# # #     {"role": "system", "content": "about c s d, computer science and design engineering is a new branch of b tech degree in government engineering college kozhikode"},
# # #     {"role": "system", "content": "provide simple answers for simple questions give details but in limited words"},
# # #     {"role": "system", "content": "answer each question independently without referencing previous questions"},
# # #     {"role": "system", "content": "consider each question and answer as seperate and give question and answer separately , only refer previous question and answer if needed very much"},
# # #     {"role": "system", "content": "don't talk about openai or chat gpt or any information regarding you are chat gpt or you have limited information till 2021 and all, only provide information to what is being asked AND DON'T TELL ANYTHING RELATED TO CHATGPT"},
# # # ]

# # # def GPT(*args):
# # #     global messages
# # #     assert args != ()

# # #     message = ' '.join(args)
# # #     messages.append({'role': 'user', 'content': message})

# # #     providers = [
# # #         # g4f.Provider.FreeChatgpt,
# # #         # g4f.Provider.Chatgpt4Online,
# # #         g4f.Provider.HuggingChat,
# # #         g4f.Provider.AmigoChat,
# # #         g4f.Provider.ChatHub
# # #     ]

# # #     for provider in providers:
# # #         try:
# # #             response = g4f.ChatCompletion.create(
# # #                 model="gpt-3.5-turbo",
# # #                 provider=provider,
# # #                 messages=messages
# # #             )
            
# # #             # Debugging the response structure
# # #             print("Raw response from", provider.__name__, ":", response)
# # #             if isinstance(response, dict) and 'choices' in response:
# # #                 ms = response['choices'][0]['message']['content']
# # #             else:
# # #                 ms = response or "   "

# # #             print("Processed message:", ms)  # Print for debugging
# # #             speak(ms)
# # #             messages.append({'role': 'assistant', 'content': ms})
# # #             return ms
# # #         except Exception as e:
# # #             print(f"Error with provider {provider.__name__}: {e}")
# # #             continue  # Try the next provider if an error occurs

# # #     return "Sorry, something went wrong with all providers."

# # # def find_code(text):
# # #     pattern = r'```python(.*?)```'
# # #     matches = re.findall(pattern, text, re.DOTALL)
# # #     if matches:
# # #         return matches[0].strip()
# # #     else:
# # #         return None

# # # while True:
# # #     query = take_command()
# # #     if query != '-':
# # #         print('User query:', query)
# # #         response = GPT(query)
# # #         python_code = find_code(response)

# # #         if python_code:
# # #             response = response.replace(python_code, '').replace('python', '').replace('```', '')
# # #             speak(response)
# # #             try:
# # #                 exec(python_code)
# # #             except Exception as e:
# # #                 print(f"Error executing code: {e}")
# # #         else:
# # #             speak(response)
# # #     else:
# # #         pass

















# # # import g4f
# # # import re
# # # import pyttsx3
# # # import speech_recognition as sr
# # # import tkinter as tk
# # # from tkinter import scrolledtext
# # # from textblob import TextBlob  # For sentiment analysis
# # # import random
# # # import threading

# # # # Initialize the speech engine
# # # engine = pyttsx3.init()

# # # # Message history
# # # messages = [
# # #     {"role": "system", "content": "Your name is MoodBot. You are designed to respond to users' queries and detect their mood."},
# # #     {"role": "system", "content": "Provide fun responses based on user mood."},
# # # ]

# # # fun_responses = {
# # #     "happy": ["That's great to hear! Why don't you tell me a joke?", "I'm glad you're happy! Keep smiling! 😊"],
# # #     "sad": ["I'm here for you! Want to talk about it?", "It's okay to feel sad sometimes. How can I cheer you up?"],
# # #     "neutral": ["That's interesting! How about we chat about something fun?", "What else is on your mind?"],
# # # }

# # # def GPT(message):
# # #     global messages
# # #     messages.append({'role': 'user', 'content': message})

# # #     providers = [
# # #         g4f.Provider.HuggingChat,
# # #         g4f.Provider.AmigoChat,
# # #         g4f.Provider.ChatHub
# # #     ]

# # #     for provider in providers:
# # #         try:
# # #             response = g4f.ChatCompletion.create(
# # #                 model="gpt-3.5-turbo",
# # #                 provider=provider,
# # #                 messages=messages
# # #             )

# # #             if isinstance(response, dict) and 'choices' in response:
# # #                 ms = response['choices'][0]['message']['content']
# # #             else:
# # #                 ms = response or "   "

# # #             # Update message history and respond
# # #             messages.append({'role': 'assistant', 'content': ms})
# # #             return ms
# # #         except Exception as e:
# # #             print(f"Error with provider {provider.__name__}: {e}")
# # #             continue

# # #     return "Sorry, something went wrong with all providers."

# # # def speak(text):
# # #     engine.say(text)
# # #     engine.runAndWait()

# # # def listen():
# # #     r = sr.Recognizer()
# # #     with sr.Microphone() as source:
# # #         print("Listening...")
# # #         audio = r.listen(source)
# # #     try:
# # #         user_query = r.recognize_google(audio)
# # #         print(f"User query: {user_query}")
# # #         return user_query
# # #     except sr.UnknownValueError:
# # #         print("Could not understand audio")
# # #         return None
# # #     except sr.RequestError as e:
# # #         print(f"Error with the API request: {e}")
# # #         return None

# # # def analyze_mood(text):
# # #     analysis = TextBlob(text)
# # #     if analysis.sentiment.polarity > 0.1:
# # #         return "happy"
# # #     elif analysis.sentiment.polarity < -0.1:
# # #         return "sad"
# # #     else:
# # #         return "neutral"

# # # def handle_query(query):
# # #     mood = analyze_mood(query)
# # #     response = GPT(query)

# # #     # Select fun response based on mood
# # #     fun_response = random.choice(fun_responses.get(mood, ["I'm here for you!"]))
    
# # #     # Speak and return the response
# # #     speak(response)
# # #     speak(fun_response)
# # #     return response, fun_response

# # # def run_moodbot():
# # #     while True:
# # #         query = listen()
# # #         if query:
# # #             print('User query:', query)
# # #             handle_query(query)

# # # def send_query():
# # #     user_input = input_box.get()
# # #     if user_input.strip():
# # #         print(f'User query (text): {user_input}')
# # #         response, fun_response = handle_query(user_input)
        
# # #         # Update the response box with the query and responses
# # #         response_box.configure(state=tk.NORMAL)
# # #         response_box.insert(tk.END, f"You: {user_input}\n")
# # #         response_box.insert(tk.END, f"MoodBot: {response}\n")
# # #         response_box.insert(tk.END, f"MoodBot (fun): {fun_response}\n\n")
# # #         response_box.configure(state=tk.DISABLED)
        
# # #         input_box.delete(0, tk.END)  # Clear the input box

# # # # Set up the UI
# # # window = tk.Tk()
# # # window.title("MoodBot")
# # # window.geometry("400x600")

# # # # Create a scrolled text area for responses
# # # response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
# # # response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# # # # Input box for text queries
# # # input_box = tk.Entry(window, width=50)
# # # input_box.pack(pady=10)

# # # # Send button for text input
# # # send_button = tk.Button(window, text="Send", command=send_query)
# # # send_button.pack()

# # # # Start the MoodBot processing in the background
# # # threading.Thread(target=run_moodbot, daemon=True).start()

# # # window.mainloop()





# # import g4f
# # import pyttsx3
# # import speech_recognition as sr
# # import tkinter as tk
# # from tkinter import scrolledtext
# # import cv2
# # import threading
# # import random
# # from fer import FER

# # # Initialize the speech engine
# # engine = pyttsx3.init()

# # # Message history
# # messages = [
# #     {"role": "system", "content": "Your name is MoodBot. You are designed to respond to users' queries and detect their mood."},
# #     {"role": "system", "content": "Provide fun responses based on user mood."},
# # ]

# # fun_responses = {
# #     "happy": ["That's great to hear! Why don't you tell me a joke?", "I'm glad you're happy! Keep smiling! 😊"],
# #     "sad": ["I'm here for you! Want to talk about it?", "It's okay to feel sad sometimes. How can I cheer you up?"],
# #     "neutral": ["That's interesting! How about we chat about something fun?", "What else is on your mind?"],
# # }

# # def GPT(message):
# #     global messages
# #     messages.append({'role': 'user', 'content': message})

# #     providers = [
# #         g4f.Provider.HuggingChat,
# #         g4f.Provider.AmigoChat,
# #         g4f.Provider.ChatHub
# #     ]

# #     for provider in providers:
# #         try:
# #             response = g4f.ChatCompletion.create(
# #                 model="gpt-3.5-turbo",
# #                 provider=provider,
# #                 messages=messages
# #             )

# #             if isinstance(response, dict) and 'choices' in response:
# #                 ms = response['choices'][0]['message']['content']
# #             else:
# #                 ms = response or "   "

# #             messages.append({'role': 'assistant', 'content': ms})
# #             return ms
# #         except Exception as e:
# #             print(f"Error with provider {provider.__name__}: {e}")
# #             continue

# #     return "Sorry, something went wrong with all providers."

# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # def listen():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         audio = r.listen(source)
# #     try:
# #         user_query = r.recognize_google(audio)
# #         print(f"User query: {user_query}")
# #         return user_query
# #     except sr.UnknownValueError:
# #         print("Could not understand audio")
# #         return None
# #     except sr.RequestError as e:
# #         print(f"Error with the API request: {e}")
# #         return None

# # def analyze_mood(face_expression):
# #     if face_expression == "happy":
# #         return "happy"
# #     elif face_expression == "sad":
# #         return "sad"
# #     else:
# #         return "neutral"

# # def detect_face_expression():
# #     # Initialize the FER emotion detector
# #     detector = FER()
    
# #     # Initialize the webcam
# #     cap = cv2.VideoCapture(0)

# #     while True:
# #         ret, frame = cap.read()
# #         if not ret:
# #             break

# #         # Detect emotions in the frame
# #         emotions = detector.detect_emotions(frame)
        
# #         if emotions:
# #             # Get the most prominent emotion
# #             dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
# #         else:
# #             dominant_emotion = "neutral"

# #         # Display the detected emotion
# #         print(f"Detected emotion: {dominant_emotion}")

# #         # Display the frame with the emotion on the screen
# #         cv2.putText(frame, f'Emotion: {dominant_emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
# #         cv2.imshow('Video', frame)

# #         # Break the loop on 'q' key press
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             break

# #     cap.release()
# #     cv2.destroyAllWindows()
# #     return dominant_emotion

# # def handle_query(query):
# #     # Detect mood using facial expression recognition
# #     face_expression = detect_face_expression()
# #     mood = analyze_mood(face_expression)

# #     # Get response from GPT
# #     response = GPT(query)

# #     # Select fun response based on mood
# #     fun_response = random.choice(fun_responses.get(mood, ["I'm here for you!"]))
    
# #     # Speak and return the response
# #     speak(response)
# #     speak(fun_response)
# #     return response, fun_response

# # def send_query():
# #     user_input = input_box.get()
# #     if user_input.strip():
# #         response, fun_response = handle_query(user_input)
        
# #         # Update the response box with the query and responses
# #         response_box.configure(state=tk.NORMAL)
# #         response_box.insert(tk.END, f"You: {user_input}\n")
# #         response_box.insert(tk.END, f"MoodBot: {response}\n")
# #         response_box.insert(tk.END, f"MoodBot (fun): {fun_response}\n\n")
# #         response_box.configure(state=tk.DISABLED)
        
# #         input_box.delete(0, tk.END)  # Clear the input box

# # # Start the listening thread
# # def listen_thread():
# #     while True:
# #         user_query = listen()
# #         if user_query:
# #             send_query(user_query)

# # # Set up the UI
# # window = tk.Tk()
# # window.title("MoodBot")
# # window.geometry("400x600")

# # # Create a scrolled text area for responses
# # response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
# # response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# # # Input box for text queries
# # input_box = tk.Entry(window, width=50)
# # input_box.pack(pady=10)

# # # Send button for text input
# # send_button = tk.Button(window, text="Send", command=send_query)
# # send_button.pack()

# # # Start listening in a separate thread
# # threading.Thread(target=listen_thread, daemon=True).start()

# # window.mainloop()











# import g4f
# import pyttsx3
# import speech_recognition as sr
# import tkinter as tk
# from tkinter import scrolledtext
# import cv2
# import threading
# import random
# from collections import Counter
# from fer import FER  # Importing FER for emotion detection

# # Initialize the speech engine
# engine = pyttsx3.init()

# # Message history
# messages = [
#     {"role": "system", "content": "Your name is MoodBot. You are designed to respond to users' queries and detect their mood."},
#     {"role": "system", "content": "Provide fun responses based on user mood."},
# ]


# fun_responses = {
#     "happy": ["That's great to hear! Why don't you tell me a joke?", "I'm glad you're happy! Keep smiling! 😊"],
#     "sad": ["I'm here for you! Want to talk about it?", "It's okay to feel sad sometimes. How can I cheer you up?"],
#     "neutral": ["That's interesting! How about we chat about something fun?", "What else is on your mind?"],
# }
# detector = FER()

# def GPT(message, mood):
#     global messages
#     messages.append({'role': 'user', 'content': f"{message} (mood: {mood})"})  # Include mood in the message

#     providers = [
#         g4f.Provider.HuggingChat,
#         g4f.Provider.AmigoChat,
#         g4f.Provider.ChatHub
#     ]

#     for provider in providers:
#         try:
#             response = g4f.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 provider=provider,
#                 messages=messages
#             )

#             if isinstance(response, dict) and 'choices' in response:
#                 ms = response['choices'][0]['message']['content']
#             else:
#                 ms = response or "   "

#             messages.append({'role': 'assistant', 'content': ms})
#             return ms
#         except Exception as e:
#             print(f"Error with provider {provider.__name__}: {e}")
#             continue

#     return "Sorry, something went wrong with all providers."

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#     try:
#         user_query = r.recognize_google(audio)
#         print(f"User query: {user_query}")
#         return user_query
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return None
#     except sr.RequestError as e:
#         print(f"Error with the API request: {e}")
#         return None

# def detect_mood():
#     cap = cv2.VideoCapture(0)
#     emotions_detected = []

#     for _ in range(10):  # Capture 10 frames
#         ret, frame = cap.read()
#         if ret:
#             emotions = detector.detect_emotions(frame)
#             if emotions:
#                 # Get the dominant emotion from the detected emotions
#                 dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
#                 emotions_detected.append(dominant_emotion)
#                 print(f"Detected emotion: {dominant_emotion}")

#         # Optional: Show the webcam feed
#         cv2.imshow('Face Detection', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     # Determine the most frequent emotion
#     if emotions_detected:
#         most_common_emotion = Counter(emotions_detected).most_common(1)[0][0]
#     else:
#         most_common_emotion = "neutral"

#     print(f"Most common detected emotion: {most_common_emotion}")
#     return most_common_emotion

# def handle_query(query):
#     # Capture mood using facial expression recognition
#     mood = detect_mood()

#     # Get response from GPT
#     response = GPT(query, mood)

#     # Select fun response based on mood
#     fun_response = random.choice(fun_responses.get(mood, ["I'm here for you!"]))
    
#     # Speak and return the response
#     speak(response)
#     speak(fun_response)
#     return response, fun_response

# def send_query(query):
#     if query.strip():
#         response, fun_response = handle_query(query)
        
#         # Update the response box with the query and responses
#         response_box.configure(state=tk.NORMAL)
#         response_box.insert(tk.END, f"You: {query}\n")
#         response_box.insert(tk.END, f"MoodBot: {response}\n")
#         response_box.insert(tk.END, f"MoodBot (fun): {fun_response}\n\n")
#         response_box.configure(state=tk.DISABLED)

# # Start the listening thread
# def listen_thread():
#     while True:
#         user_query = listen()
#         if user_query:
#             send_query(user_query)

# # Set up the UI
# window = tk.Tk()
# window.title("MoodBot")
# window.geometry("400x600")

# # Create a scrolled text area for responses
# response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
# response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# # Input box for text queries
# input_box = tk.Entry(window, width=50)
# input_box.pack(pady=10)

# # Send button for text input
# send_button = tk.Button(window, text="Send", command=lambda: send_query(input_box.get()))
# send_button.pack()

# # Function to quit the application
# def quit_application():
#     cv2.destroyAllWindows()  # Ensure camera window is closed
#     window.quit()

# # Stop all operations
# def stop_all():
#     cv2.destroyAllWindows()
#     window.quit()  # Quit the application

# # Add a button to stop all operations
# stop_button = tk.Button(window, text="Stop All", command=stop_all)
# stop_button.pack(pady=10)

# # Bind the quit function to the 'q' key
# window.bind('<q>', lambda event: quit_application())

# # Handle Enter key to send the input
# def on_enter(event):
#     send_query(input_box.get())
#     input_box.delete(0, tk.END)  # Clear the input box after sending

# # Bind the Enter key to the input box
# input_box.bind('<Return>', on_enter)

# # Start listening in a separate thread
# threading.Thread(target=listen_thread, daemon=True).start()

# window.mainloop()


import g4f
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
import cv2
import threading
import random
from collections import Counter
from fer import FER  # Importing FER for emotion detection

# Initialize the speech engine
engine = pyttsx3.init()

# Message history
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
    messages.append({'role': 'user', 'content': f"{message} (mood: {mood})"})  # Include mood in the message

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

    for _ in range(10):  # Capture 10 frames
        ret, frame = cap.read()
        if ret:
            emotions = detector.detect_emotions(frame)
            if emotions:
                # Get the dominant emotion from the detected emotions
                dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
                emotions_detected.append(dominant_emotion)
                print(f"Detected emotion: {dominant_emotion}")

        # Optional: Show the webcam feed
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Determine the most frequent emotion
    if emotions_detected:
        most_common_emotion = Counter(emotions_detected).most_common(1)[0][0]
    else:
        most_common_emotion = "neutral"

    print(f"Most common detected emotion: {most_common_emotion}")
    return most_common_emotion

def handle_query(query):
    # Capture mood using facial expression recognition
    mood = detect_mood()

    # Get response from GPT
    response = GPT(query, mood)

    # Select fun response based on mood
    fun_response = random.choice(fun_responses.get(mood, ["I'm here for you!"]))
    
    # Speak and return the response
    speak(response)
    speak(fun_response)
    return response, fun_response

def send_query(query):
    if query.strip():
        response, fun_response = handle_query(query)
        
        # Update the response box with the query and responses
        response_box.configure(state=tk.NORMAL)
        response_box.insert(tk.END, f"You: {query}\n")
        response_box.insert(tk.END, f"MoodBot: {response}\n")
        response_box.insert(tk.END, f"MoodBot (fun): {fun_response}\n\n")
        response_box.configure(state=tk.DISABLED)

# Start the listening thread
def listen_thread():
    while True:
        user_query = listen()
        if user_query:
            send_query(user_query)

# Set up the UI
window = tk.Tk()
window.title("MoodBot")
window.geometry("400x600")

# Create a scrolled text area for responses
response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input box for text queries
input_box = tk.Entry(window, width=50)
input_box.pack(pady=10)

# Send button for text input
send_button = tk.Button(window, text="Send", command=lambda: send_query(input_box.get()))
send_button.pack()

# Function to quit the application
def quit_application():
    cv2.destroyAllWindows()  # Ensure camera window is closed
    window.quit()

# Stop all operations
def stop_all():
    cv2.destroyAllWindows()
    window.quit()  # Quit the application

# Add a button to stop all operations
stop_button = tk.Button(window, text="Stop All", command=stop_all)
stop_button.pack(pady=10)

# Bind the quit function to the 'q' key
window.bind('<q>', lambda event: quit_application())

# Handle Enter key to send the input
def on_enter(event):
    send_query(input_box.get())
    input_box.delete(0, tk.END)  # Clear the input box after sending

# Bind the Enter key to the input box
input_box.bind('<Return>', on_enter)

# Start listening in a separate thread
threading.Thread(target=listen_thread, daemon=True).start()

window.mainloop()
