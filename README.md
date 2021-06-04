# Car Api  
## Live Site:  
https://pacific-taiga-60618.herokuapp.com/api/ford/f-150/2017  
(Clicking this link will bring up serveral JSON objects containing data that relates to Ford F-150's from the year 2017,   
read *access data using urls paths* below and try putting some different values in the url)

### This Api is Restful

### It serves over 6000 articles of car data in the form of Json objects

**Access data using urls paths:** 

**/api/** check site Health  
**/api/all** get all data  
**/api/id** get a single data object by a numerical id (all the data has ordered numberic values ranging from 1-6516), so /api/100, would grab the 100th object of data.  
**/api/make/** grabs all data objects associated with certain make of car  
**/api/make/model/** grabs all data objects associated with certain make and model of car  
**/api/make/model/year/** grabs all data objects associated with certain make, model and year of car
  
I used django-import-export to import a csv file into a mysql database, specifically using the import function in the django admin panel 

**Some commands to help you get rolling:**   
create a virtual environment:   
> python3 -m venv  

Activate Virtual environment:  
>source venv/bin/activate 

Install the specified requirements:
>pip install -r requirements.txt

Write a requirements.txt file:
>pip freeze > requirements.txt  

Run dev server:
>python manage.py runserver

Migrate to database:
>python manage.py migrate

Commit updates to database:
>python manage.py makemigrations

Intergated Cli tool for testing:
>python manage.py shell

For deployment I used an AWS ec2 instance that runs ubuntu 18.04, which serves data to a mysql database that is hosted on AWS RDS.  
I used nginx and uwsgi (uwsgi is similar to gunicorn) to serve to website. 

(I moved my deployment to Heroku, so this isn't needed, but it still helpful in linux server deploy scenarios) 

**Here is my nginx conf file*:*  

    upstream django {  
    server unix:///home/ubuntu/carApi/djangoApi.sock;  
    }  
    server {  
    listen      80;  
    server_name ec2-54-245-43-7.us-west-2.compute.amazonaws.com www.ec2-54-245-43-7.us-west-2.compute.amazonaws.com;  
    charset     utf-8;  
     
    client_max_body_size 75M;  
    
    location /static {  
        alias /home/ubuntu/carApi/static;  
        }  
     
    location / {  
        uwsgi_pass  django;  
        include     /home/ubuntu/carApi/uwsgi_params;  
        }  
    }  
