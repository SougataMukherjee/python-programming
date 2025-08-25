import streamlit as st
import speech_recognition as sr
from groq import Groq
from gtts import gTTS
import os
import pygame
from dotenv import load_dotenv
import tempfile

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# Initialize pygame mixer (only once)
if not pygame.mixer.get_init():
    pygame.mixer.init()

st.title("🎙️ Realtime Voice Bot")
st.write("Talk to me, I will listen and reply with my voice 👂🤖")

# 🎤 Function: Speech Recognition
def listen_and_convert():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        st.success(f"🗣 You said: {query}")
        return query
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio")
        return None

# 🤖 Function: Get AI response from Groq
def get_groq_response(query):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Reply like a human in max 2-3 short lines."},
                {"role": "user", "content": query}
            ],
            model="llama-3.1-8b-instant",   # try with gemma-7b-it if fails
            max_tokens=150,
            temperature=0.7
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error from Groq: {str(e)}"

# 🔊 Function: Convert Text to Speech and Play
def speak_text(text):
    # If old speech is running → stop it
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    # Generate new speech
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
        tts = gTTS(text=text, lang="en")
        tts.save(fp.name)
        audio_file_path = fp.name

    # Play new speech
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

# 🎛 Button to Start Interaction
if st.button("🎙️ Start Talking"):
    query = listen_and_convert()
    if query:
        response = get_groq_response(query)
        st.write(f"🤖 AI: {response}")
        speak_text(response)
