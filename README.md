# django_image
Simple upload example using python framework Django

Tools used
-------------
- Pyhton v2.7.3
- Pip
- Django v1.8
- Pillow v3.4.1

Manual Installation
-------------
### 1.Pip
To install Django first you need to install **Pip**. Download this .py file frome here https://bootstrap.pypa.io/get-pip.py and install it using python as follow.
> $python get-pip.py

### 2.Django
To instal Django use this.
> $pip install Django==x.x

### 3.Pillow
To instal Django use this.
> $pip install Pillow

Vagrant Installation
-------------
### 1.VirtualBox
Install the latest version of VirtualBox https://www.virtualbox.org/

### 2.Vagrant
Install the latest version of Vagrant https://www.vagrantup.com/

### 3.Download vagrant box
To download the vagrant box with this project and all the tools needed to run it follow this steps.

3.1 Make a new directory and initialize it with vagrant
```
$ mkdir vagrant_django
$ cd vagrant_django
$ vagrant init MilesD/vagrant-django
```
3.2 In the Vagrantfile recentrly created add this line
```
config.vm.network "forwarded_port", guest: 8000, host: 8000
```
3.3 Download and run the Vagrant box using the command up
```
vagrant up
```
3.4 Now you can SSH into the box with this url **127.0.0.1:2222** and using **"vagrant"** as user and password. The project is located in the user folder **/home/vagrant/**

How to run
-------------
Browse to the root of the repository where the manage.py file is located and execute this.
>$ pyhton manage.py runserver 0.0.0.0:8000

And run it in your favorite broser using the next url.
>http://localhost:8000/updload
