# Car Api

## This Api is Restful

### It serves over 6000 articles of car data in the form of Json objects

**access data using urls paths** 

**/api/** check site Health  
**/api/all** get all data  
**/api/<id>** get a single data object by a numerical id (all the data has ordered numberic values ranging from 1-6516), so /api/100, would grab the 100th object of data.
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
