check python --version
check pip --version
python -m venv venv
pip install fastapi uvicorn
uvicorn main:app --reload