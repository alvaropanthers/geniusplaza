# geniusplaza

Installation instructions

create a new virtual enviroment:  
virtualenv env  

activate virtual env with:  
source env/bin/activate  

install django and djangorestframework:  
pip install django djangorestframework  

in project make migrations and migrate:  
python manage.py makemigrations  
python manage.py migrate  

load sample data  
python manage.py loaddata data.json  
