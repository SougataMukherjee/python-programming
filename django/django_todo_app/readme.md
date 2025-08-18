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
from . import forms #import form from current directory 
from django.urls import path # Importing path to define URLs
from .models import Rest #import model rest from current directory 
class Reserve(forms.Form): # when user sent get request to form return response as hello
  def get(self,request):
     return HttpResponse("hello")

#URL patterns (mapping URLs to views)
urlpatterns=[
	path('function',view.hello) #function based view
	path('class',view.view()) #class based view
	path('app/',include('appname'))
]

#return first name when object is printed
def __str__(self):
   reyturn self.first_name
