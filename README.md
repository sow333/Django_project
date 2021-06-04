# Django Files structure 
Django uses a directory structure to arrange the different parts of the web application. Now, we will learn about the Django app structure and the project structure in further detail here.

##Django Project Structure 
This is what the default Django project structure looks like. Let’s understand the functions of the files that are shown in the above image to help you get a context of what a project folder consists of.

## 1. Manage.py
This file is used basically as a command-line utility and for deploying, debugging, or running our web application.

This file contains code for runserver, or makemigrations or migrations, etc. that we use in the shell. Anyway, we do not need to make any changes to the file.

runserver: This command is used to run the server for our web application.
Migration: This is used for applying the changes done to our models into the database. That is if we make any changes to our database then we use migrate command. This is used the first time we create a database.
Makemigration: this is done to apply new migrations that have been carried out due to the changes in the database. 
This image is just for your reference. You don’t have to understand the code written here since we are not changing anything here.

## 2. _init_.py
This file remains empty and is present their only to tell that this particular directory(in this case django_project) is a package.We won’t be doing any changes to this file as well.  

## 3. setting.py
This file is present for adding all the applications and the middleware application present. Also, it has information about templates and databases. Overall, this is the main file of our Django web application.

## 4. urls.py
This file handles all the URLs of our web application. This file has the lists of all the endpoints that we will have for our website.URL: Universal Resource Locator is used to provide the addresses of the resources (like image, website, etc) that are present there on the internet. 

## 5. wsgi.py
This file mainly concerns with the WSGI server and is used for deploying our applications on to servers like Apache etc.WSGI, short for Web Server Gateway Interface can be thought of as a specification that describes how the servers interact with web applications.

Again we won’t be doing any changes to this file.  

You don’t have to understand the code written here since we are not changing anything here.

## 6. asgi.py
In the newer versions of Django, you will also find a file named as asgi.py apart from wsgi.py. ASGI can be considered as a succeeder interface to the WSGI.
ASGI, short for Asynchronous Server Gateway interface also has the work similar to WSGI but this is better than the previous one as it gives better freedom in Django development. That’s why WSGI is now being increasingly replaced by ASGI.Again we won’t be doing any changes to this file.


## 7. APPs
Apart from the above file, our project contains all the app directories. Now we will look into the Django app structure in detail

## Django App Structure 

## 1. _init_.py
This file has the same functionality just as in the _init_.py file in the Django project structure. It remains empty and is present just to indicate that the specific app directory is a package.No changes need to be made to the file manually. 

## 2. admin.py
As the name suggests, this file is used for registering the models into the Django administration.The models that are present have a superuser/admin who can control the information that is being stored. 

## 3. apps.py
This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases and hence we won’t be doing anything here in the beginning. 

## 4. models.py
This file contains the models of our web applications (usually as classes).Models are basically the blueprints of the database we are using and hence contain the information regarding attributes and the fields etc of the database.

## 5. views.py
This file is a crucial one, it contains all the Views(usually as classes). Views.py can be considered as a file that interacts with the client. Views are a user interface for what we see when we render a Django Web application. We are going to make different types of Views using the concept of serializers in the Django Rest_Framework in the further sections. 

## 6. urls.py
Just like the project urls.py file, this file handles all the URLs of our web application. This file is just to link the Views in the app with the host web URL. The settings urls.py has the endpoints corresponding to the Views. 

## 7. tests.py
This file contains the code that contains different test cases for the application. It is used to test the working of the application.We won’t be working on this file in the beginning and hence it is going to be empty as of now.
