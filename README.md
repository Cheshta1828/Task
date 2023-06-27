# Task
#step 1:Clone the Repository:
COMMAND: 
#step 2:Install Dependencies:
COMMAND :  pip install -r requirements.txt
#step 3:change directory to task
COMMAND :cd task
#step 4:Create a Virtual Environment (Optional but Recommended):
COMMANDS:
python -m venv myenv       # Create a new virtual environment
myenv\Scripts\activate     # Activate the virtual environment (for Windows)
#step 5:Install Dependencies (Inside the Virtual Environment):
COMMAND :
myenv\Scripts\activate 

#step6:DATABASE SETUP
update the database settings in the project's settings.py file.
Provide details such as the MySQL database engine, name, user, password, host, and port to be used.
#step 7:Make the necessary migrations
COMMAND: python manage.py makemigrations
COMMAND: python manage.py migrate
#step 8: run the server 
COMMAND :python manage.py runserver 
Superuser Creation (Optional):
To access admin interface we need to Create a Superuser (Optional):
COMMAND: python manage.py createsuperuser
then go to localhost/admin to see databases








