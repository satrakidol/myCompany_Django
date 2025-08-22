pip install django

 django-admin startproject company
 manage.py startapp myCompany

Create Project
django-admin startproject company
python manage.py startapp myCompany

Run Project
python manage.py runserver

Migrate Database-Models
python manage.py makemigrations
python manage.py migrate

Create Superuser (Admin)
python manage.py createsuperuser

Clear Session

python manage.py shell

from django.contrib.sessions.models import Session
Session.objects.all().delete()


