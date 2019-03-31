# fossee1

Project for IITB summer Internship Entrance


- Clone the repo
``` 
git clone https://github.com/mananpoddar/fossee1
cd fossee1/mysite
```
- Create a virtualenv
```
virtualenv -p python3 venv
source venv/bin/activate
```

- Install the requirements
```
pip install -r requirements.txt
```
- Setup your mysql database and sync it with my project
```
go to fossee1/mysite/mysite/settings.py and in DATABASE array, change the password and username to yours.
do python manage.py makemigrations
then, python manage.py migrate
```

- Run the dev server
```
python manage.py runserver
```
- request localhost:8000/fossee1

- Important directories and files to make your look up to the code easier
```
core backend logic - > fossee1/mysite/fossee1/views.py
core frontend logic - > fossee1/mysite/fossee1/static/fossee1/ajax.js
templates(html files) - > fossee1/mysite/fossee1/templates/fossee1/
routing files - > fossee1/mysite/fossee1/urls.py
'''
