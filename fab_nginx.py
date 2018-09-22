#from fabric.api import *
from fabric import Connection
#from fabric.contrib import project

 
nginx_conf = "/home/bhagyashri/virtualenv1/fab_config/default"
sites_available = "/etc/nginx/sites-available"
sites_enabled = "/etc/nginx/sites-enabled"

remote_location = "Bhagya7@github.com:Bhagya7/Fabric-Django-AWS.git:/fab_config/default"
# Main - install NGINX
#print("Connecting to EC2 instance!")
c = Connection('i-05bdb4925bf7977a3')

#print("Installing NGINX!")
result = c.run("sudo apt-get update; sudo apt install nginx; sudo apt-get install git-core; sudo chown -R ubuntu:ubuntu ~") #mkdir gitRepo;
#result = c.run("cd ~/gitRepo; git clone https://github.com/Bhagya7/Fabric-Django-AWS.git; ls ~/gitRepo; ls -R Fabric-Django-AWS")
result = c.run("sudo cp ~/gitRepo/Fabric-Django-AWS/fab_config/default /etc/nginx/sites-enabled; sudo service nginx restart")
#sudo scp %s %s; sudo service nginx restart" % (remote_location, sites_enabled))

#print("Done!")
#c.sudo("apt install nginx")

