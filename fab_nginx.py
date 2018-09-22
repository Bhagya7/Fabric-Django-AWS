#from fabric.api import *
from fabric import Connection
#from fabric.contrib import project

 
nginx_conf = "/home/bhagyashri/virtualenv1/fab_config/default"
sites_available = "/etc/nginx/sites-available"
sites_enabled = "/etc/nginx/sites-enabled"
# Main - install NGINX
#print("Connecting to EC2 instance!")
c = Connection('i-08fe404ec44f8c46e')

#print("Installing NGINX!")
result = c.run("sudo apt-get update; sudo apt install nginx; sudo cp %s %s; sudo service nginx restart" % (nginx_conf, sites_enabled))

#print("Done!")
#c.sudo("apt install nginx")

