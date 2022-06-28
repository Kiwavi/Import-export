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
While in the admin page, click on the currencies model    
After you click on currencies, click import    
The file to import should be specific to the model created in appimports.models    
In this case, a forex file is used. In case you want to use another file, ensure you have a model that corresponds with the files' fields    
The forex file is located inside the static folder of this project therefore upload it    
Once you upload, choose format as csv (the file is a .csv)   
Click submit    
Once you're done, you can confirm the file was uploaded by visiting localhost/api/forex which is an API endpoint.     
