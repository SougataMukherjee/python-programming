





# 1️⃣ Create the virtual env
python -m venv venv

# 2️⃣ Activate it
.\venv\Scripts\Activate.ps1

# 3️⃣ install fastapi
pip install fastapi uvicorn Jinja2
check install or not      pip show fastapi


# 4️⃣ run app
uvicorn main:app --reload

go to the url like http://127.0.0.1:8000

# 5️⃣ Deactivate
deactivate


