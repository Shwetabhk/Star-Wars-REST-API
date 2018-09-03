# Star-Wars-Rest-API

Star Wars REST API/Backend app https://whispering-caverns-86180.herokuapp.com/    

The website is hosted on Heroku
the link is
    https://whispering-caverns-86180.herokuapp.com/add_planets/


This app runs on Python 3.6. Make sure you have Python 3.6 and pip installed.


# Clone the Repository

Open the terminal and run the command:

		git clone https://github.com/Shwetabhk/Star-Wars-.git

# Create a virtual environment

open your working directory in the terminal and run the following commands:

		pip install virtualenv

		python -m virtualenv SWENV

		source SWENV/bin/activate


# Install the requirements

Open the cloned folder in the terminal(virtual environment) and run the following commands:

		pip install -r requirements.txt


# Run the following command

	python manage.py collectstatic


# Run the server

		python manage.py runserver
    
Now open the app in localhost:8000
