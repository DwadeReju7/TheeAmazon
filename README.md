My application domain was meant to capture necessary data for an e-commerce website. For this site I wanted to capture the necessary information and created 5 tables. These tables included Categories, Customers, Order_Items, Orders and Products. 

In  order to set up the project I had to first start a virtual environment. To do that i typed python3 -m venv venv. After that I typed in source venv/bin/activate. After that I pip installed django so it would be available in our virtual environment. It was very important to include all the information including " pip install django~=5.2 "psycopg[binary]" django-environ " this caused an issue for us later. In regards to installing requirements I didn't do this until the end but I had to run "pip freeze > requirements.txt ". 

To create an .env file to include in my overall folder. In regards to the credntials before testing this on my local environment I had my actual credentials. For the purpose of submitted this assignment as directed at the end, I replaced it with example data. 

Running migrations took me the longest time because I kept running into errors. This included making edits on my settings.py and ensuring that myapp was in the correct directory. After creating the migration using " PS > python3 manage.py makemigrations myapp " I then ran " PS> python manage.py migrate ". Afterwards we ran python3 manage.py createsuperuser where we were prompted to create a username and password. After confirming that we would run the server using " PS> $ python manage.py runserver` "

