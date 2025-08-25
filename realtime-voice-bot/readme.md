python -m venv .venv
.venv\Scripts\activate 

pip install streamlit speechrecognition pyaudio groq python-dotenv

pip install -r requirements.txt
streamlit run main.py