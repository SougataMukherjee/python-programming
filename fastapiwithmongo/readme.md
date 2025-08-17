
# in mongodb
database cluster connect->
username sam and password 123->choose a connecttion->drivers select python and version




# 1️⃣ Create the virtual env
python -m venv venv

# 2️⃣ Activate it
.\venv\Scripts\Activate.ps1

# 3️⃣ install fastapi
pip install fastapi uvicorn
pip install 'pymongo[srv]'
python -m pip install "pymongo[srv]==3.12"
and paste mongo file
pip install certifi


# 4️⃣ run app
uvicorn main:app --reload

go to the url like http://127.0.0.1:8000

# 5️⃣ Deactivate
deactivate


