python --version
pip --version
python -m django --version

# 1️⃣ Create the virtual env
python -m venv venv

# 2️⃣ Activate it
.\venv\Scripts\Activate.ps1

# 3️⃣ install packages
install SQLite Viewer and python extension in vs code
pip install django mysqlclient pipenv 
django-admin startproject todoproject 

# 4️⃣ create files
 we have to modify the index.html ,models.py,urls.py,views.py,settings.py


# 5️⃣ run this app
python manage.py startapp todoproject
python manage.py makemigrations
python manage.py migrate
every time run with:     python manage.py runserver

# create super user
python manage.py createsuperuser
create name admin ,email as admin@admin.com, password as password
python manage.py runserver
in url add /admin

# notes

flowchart LR
    A[User / Browser] --> B[Django Request Handler]
    B --> C[URL Dispatcher (urls.py)]
    C --> D[View (views.py)]
    D -->|Fetch/Save| E[Model (models.py)]
    E -->|Communicates with| F[(Database)]
    D --> G[Template (HTML, templates/)]
    G --> H[Response to User]
    F --> E
    E --> D

from . import forms #import form from current directory 
from django.urls import path # Importing path to define URLs
from .models import Rest #import model rest from current directory 

views.py -> logic that handles request → response
class Reserve(forms.Form): # when user sent get request to form return response as hello
  def get(self,request):
     return HttpResponse("<h1>Hello World</h1>") #static response
   def home(request):
    return render(request, 'home.html', {'name': 'dynamic data'}) #dynamic response

in url.py mapping URLs to views
urlpatterns=[
	path('function',view.hello) #function based view
	path('class',view.view()) #class based view
	path('app/',include('appname'))
   path('',views.home,name="home")
   path('add',views.add,name="add")
]

in templates reuse base layout along with dynamic data
{% extends 'base.html' %} 

{% block content %}
   <h1>Hello {{ name }}</h1>
{% endblock %}

#return first name when object is printed
def __str__(self):
   return self.first_name

in settings.py
INSTALLED_APPS List of all apps used in your project
MIDDLEWERE Helps in security, session management, authentication
TEMPLATE Tells Django where HTML templates are stored.Inside "DIRS" you give path of your templates folder.
DATABASE bydefault sqllite,you can change mysql,mongo later
STATIC_URL='/static/'  # URL to access static files (CSS, JS, images)
STATICFILES_DIRS=[     # Where your development static files are
 os.path.join(BASE_DIR,'/static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'assets') # Where Django collects all static files for production


