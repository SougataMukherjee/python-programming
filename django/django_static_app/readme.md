python --version
pip --version
python -m django --version

# 1️⃣ Create the virtual env
python -m venv venv

# 2️⃣ Activate it
.\venv\Scripts\Activate.ps1

# 3️⃣ install packages

pip install django 
django-admin startproject config .
python manage.py startapp core 

# 4️⃣ create files
Create these folders at the project root:
├─ templates/
│  └─ base.html
│  └─ home.html
├─ static/
│  ├─ css/
│  │  └─ style.css
│  ├─ js/
│  │  └─ app.js
│  └─ img/
│     └─ logo.png 
 
 in config/settings.py add 'core' in INSTALLED_APPS
                       add 'DIRS': [ BASE_DIR / 'templates' ], in TEMPLATES
                       STATIC_URL = 'static/'
                       STATICFILES_DIRS = [ BASE_DIR / 'static' ] 

in core/view.py add def home(request):
    return render(request, 'home.html')
and config/urls.py
   add path  path('', home, name='home'),

fill the template file
# 5️⃣ run this app

python manage.py migrate
python manage.py createsuperuser
create name admin ,email as admin@admin.com, password as password
every time run with:     python manage.py runserver
Homepage: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

