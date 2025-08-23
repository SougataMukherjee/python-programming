
python -m venv .venv
.venv\Scripts\activate

install
pip install langchain langchain-community langchain-groq groq python-docx pypdf streamlit
pip install unstructured[local-inference] pdfminer.six pillow pytesseract


run 
streamlit run app.py

check
pip freeze