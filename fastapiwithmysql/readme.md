
# in mysqlworkbench
rightclick create schema-> give name->apply->apply-finish
go to the left tables->right click refresh all




# 1️⃣ Create the virtual env
python -m venv venv

# 2️⃣ Activate it
.\venv\Scripts\Activate.ps1

# 3️⃣ install fastapi
pip install fastapi uvicorn sqlalchemy pymysql


# 4️⃣ run app
uvicorn main:app --reload

go to the url like http://127.0.0.1:8000/docs

# 5️⃣ Deactivate
deactivate


