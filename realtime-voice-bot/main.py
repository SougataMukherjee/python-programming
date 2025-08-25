import streamlit as st
import speech_recognition as sr
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Realtime Voice Bot", layout="centered")
st.title("🎤 Realtime Voice Bot (Mic → Text → Groq Response)")

# Recognizer
recognizer = sr.Recognizer()

if st.button("🎙️ Speak Now"):
    with sr.Microphone() as source:
        st.info("Listening... Speak something!")
        audio = recognizer.listen(source, phrase_time_limit=5)  # 5 sec limit
        try:
            query = recognizer.recognize_google(audio)
            st.success(f"🗣️ You said: {query}")

            # Send query to Groq
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # You can change
                messages=[{"role": "user", "content": query}],
                temperature=0
            )

            bot_reply = response.choices[0].message.content
            st.write("🤖 Bot Response:")
            st.success(bot_reply)

        except sr.UnknownValueError:
            st.error("Could not understand audio, please try again!")
        except sr.RequestError as e:
            st.error(f"Error with Speech Recognition: {e}")
