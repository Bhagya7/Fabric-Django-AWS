#from fabric.api import *
from fabric import Connection
#from fabric.contrib import project

 

# Main - install NGINX
#print("Connecting to EC2 instance!")
c = Connection('i-08fe404ec44f8c46e')

#print("Installing NGINX!")
result = c.run("sudo apt-get update; sudo apt install nginx; sudo cp ~/virtualenv1/default /etc/nginx/sites-enabled; sudo service nginx restart")

#print("Done!")
#c.sudo("apt install nginx")

