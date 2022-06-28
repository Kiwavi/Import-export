# Import-export

# This project shows how to upload a file into the database using the django import-export package    
Get started    
Clone this repository into a preferably empty folder   
`git clone https://github.com/Kiwavi/Import-export.git .     `   
create a virtual environment    
`python -m venv venv    `
Activate the virtual environment         
`source venv/bin/activate `   
Create superuser    
`python manage.py createsuperuser    `
Once you create superuser, run migrations    
`python manage.py migrate`    
Visit the python admin page on your browser 127.0.0.1:8000/admin    
Login using the admin credentials you created    
