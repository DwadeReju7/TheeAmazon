(DJANGO Assignment 01)
My application domain was meant to capture necessary data for an e-commerce website. For this site I wanted to capture the necessary information and created 5 tables. These tables included Categories, Customers, Order_Items, Orders and Products. 

In  order to set up the project I had to first start a virtual environment. To do that i typed python3 -m venv venv. After that I typed in source venv/bin/activate. After that I pip installed django so it would be available in our virtual environment. It was very important to include all the information including " pip install django~=5.2 "psycopg[binary]" django-environ " this caused an issue for us later. In regards to installing requirements I didn't do this until the end but I had to run "pip freeze > requirements.txt ". 

To create an .env file to include in my overall folder. In regards to the credntials before testing this on my local environment I had my actual credentials. For the purpose of submitted this assignment as directed at the end, I replaced it with example data. 

Running migrations took me the longest time because I kept running into errors. This included making edits on my settings.py and ensuring that myapp was in the correct directory. After creating the migration using " PS > python3 manage.py makemigrations myapp " I then ran " PS> python manage.py migrate ". Afterwards we ran python3 manage.py createsuperuser where we were prompted to create a username and password. After confirming that we would run the server using " PS> $ python manage.py runserver` "

(DJANGO Assignment 02)
I choose to implement CRUD from my 'Products Model'. This is inclusive of name, price and category.

Myapp url was used for creating url patterns that would assist me with switching from one html document to another. 

In regards to implementing CRUD operations. C stands for Create, this is the process of creating new products to add to our e-commerce site. This is implemented directly into the browser with the information presented in urls.py. R stands for Read which is meant to view existing data that we already have set. Read can be connected to both our detail view as well as our list view to look at certain information that is already available. U stands for update which gives us a way of updating information directly to adding a new product to the table. For this we would put the integer thats tied to the product and then update. D stands for delete which gives us a way of deleting current information. 

(DJANGO Assignment 03)
With adding Google Authentication to the project. The firsts step was to go to the Gogle Cloud Console and create a new project. Through navigating those steps we were given the proper credentials to add to our .env file to store them securely. This information included a 'Client ID' as well as a 'Client Secret'. Afterwards we had to alter our settings.py with adding a dictionary entitled SOCIALACCOUNT_PROVIDERS. We would have to do this for every Auth based provider. 

In order to test login we ran our command "python3 manage.py runserver" upon getting our http link the first thing we did was add '/accounts/' to the link which took us to the sign in page. The immediate difference I noticed was the additional "Or use a third party" option that appeared with Google hyperlinked. I first focused on logging in locally to ensure I had the proper credentials. Funny enough I forgot my password but was able to login to my admin account and change my password directly there. I used the link for the Google Auth and was amazed how this looked the exact same as the process with well established sites. 

Permission restrictions on update/delete views were completed by adding UserPassesTextMixin so while I am logged in, every product I view in my inventory has update and delete options. 

(DRF Assignment 01)
The Django RestFramework was added to my settings.py under installed apps then it was given its own section as a dictionary within the document. 

The base URL for /api/ is added to our HTTP info thats loaded once we begin running the server. After putting the base url of api we can add the model and ID number that leads us to direct inputs. 

The models that are exposed in the API are CRUD (create, read, update & delete)

To test your API using a browsable API the first thing you'll have to do is run "python3 manage.py runserver". Once it gives up the HTTP response to put in the browser you'll need to ensure you are logged in so you have the proper authentication. '/api/' to the end of the browser address. 

(DRF Assignment 02)
Using the query parameters includes adding the following examples to the end of my http link in my web browser (`?field=value`, `?search=term`, `?ordering=-field`) these paramters were added to my views.py and values for the first parameter include putting in either the category or product name, the second includes adding the product name and the third is ordering only by price as set in my views document.

Pagination we set in my settings.py document with the number set to 10. By setting this each page size stops at 10 products before going to the next. With '?page=' I can select which page I want to go directly to. 

Customer permission logic is tied to each individual owner within this database. For the purpose of this project I created 2 owners, while they could view each others submissions they could not edit or delete as that was reserved for their own work. 

When testing new features a large part of this is knowing what account you want to be logged into or if you want to be logged in at all. I say this because you want to ensure your filtering, updating and deleting is all functioning. However to ensure you have a secure database you want to logout and see what permissions are available without an account (This is crucial to ensuring you have a secure database). 

(CONTAINERIZATION ASSIGNMENT 01)
You have to install docker in your terminal and then create docker files including, Dockerfile, .dockerignore and docker-compose.yml. You also want to make sure docker is on your local device so you can log in to your dashboard. When you submit docker compose up you start running the containers and view logs in real time as well as access your application via the exposed ports. 

.env.example is a sample .env file that you leave saved within your folder for any additional developers who may need guidance on how to recreate what you've built. You fill it up with dummy text. Example below:
SECRET_KEY=your-super-secret-django-key-here!@#$%^&*(-+=)
DEBUG=FALSE
DATABASE_URL=postgres://postgres:yourpassword@localhost:input/yourmodel
POSTGRES_DB=yourdatabase
POSTGRES_USER=yourusernamme
POSTGRES_PASSWORD=samplepassword
GOOGLE_CLIENT_ID=19232038-examplepulledfromgoogleclient
GOOGLE_CLIENT_SECRET=G283084-examplepulledfromgoogleclient

Running the database migrations took the longest amount of time because it was brought to my attention the variety of issues that I ran into. The first step was to do the docker compose build to build out the containers, from there you start the containers with docker compose up -d. The following steps include docker compose ps (to check status), docker compose logs -f web(to access logs). From there you will add docker compose exec and this is when I got different issues. I  was running into multiple issues connecting my docker to my Django database. I  needed to import pip install python-decouple dj-database-url. django_web kept exited with code 1 so I  must have been running into an issue for it to keep crashing. I  had to download wait-for-it.sh to ensure that my app waited for my database before starting. Luckily this worked and I was able to successfully migrate.

In order to access the running application and API I did not have to go in my venv and hit the 'runserver' command. Instead I was able to grab the link directly from my terminal and type it into my browser. In order to access my api I just needed to add '/api/' to my url. 

(DEPLOYMENT ASSIGNMENT 01)
My AWS Deployment process was very detailed yet straight forward. I first had to make sure my account was active in my AWS Management Console. From there I had to configure both an ECR and an EC2 instance. From there the next step was to push the django application to the ECR instance. This included creating the repository and taking that information to input into my local system.

ECR stands for Elastic Container Registry. This is meant to capture the images within my database and maintain a copy. Outside of ECR is my EC2 which keeps log of all my instances as well as the applicable data and information that comes with it. This will be essential when launching the browser. 

When pushing an image to your ECR the first thing you have to do is authenticate your Docker to ECR locally. This will be done using a command that includes both Docker and AWS controls. Upon authentication, you'll use docker compose to to "build" and essentially name the image. After that you'll use the ECR reposiroty URI to add to your terminal and tag that image in preparation for it to be pushed. The final step is to push the image to the ECR. 

Setting up the EC2 instance and getting it to run properly took me the longest out of each of these tasks. The first thing you'll have to do is login to AWS and launch your instance and give it a name. From there you'll establish your network settings, security groups and storage configurations. Once that is completed you can launch your instance. Upon launching the instance you'll then install docker and connect to your EC2. You'll then SSH into your EC2 instance directly on the terminal (this was cool because a little bird popped up every time it was successful). We used 'nano' to modify both .env as well as docker-compose.yml in the EC2 instance. To transfer files there were a series of docker commands starting with docker compose. 

It was important to make certain changes to our docker-compose.yml document as well as our .env for our EC2. Being as though a lot of the settings were configured locally we needed to ensure that they would transfer over to our EC2 instance as well. You want to be sure to modify the docker-compose.yml so you are able to input the image from the ECR into the document. With this step it is important to remove volume mount as well, because the only code should be coming from ECR image. The next step was to modify the command so migrations will run automatically. For .env you would use DEBUG=False in order to address security, this is important. Once you go into ALLOWED_HOST you would input the EC2 Public IP. CSRF_TRUSTED_ORIGINS to avoid 403 errors. 

docker compose up -d is the first command that pulls the image and starts the app and database containers in detached mode. docker compose exec web python manage.py migrate applies database migrations inside the running Django container (web service) to ensure the database schema is up to date.




