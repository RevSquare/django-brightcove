#################
Django Brightcove
#################

Manages the integration of brightcove videos in a django project. It extends the the Bricove librairy developped by Jonathan Beluch: https://pypi.python.org/pypi/brightcove/0.2

It basically add a form field to easily integrate brightcove account video in the django admin or any form. And adds a template tag to fast integrate a brightcove video in a template.

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

Add this line to your requirements.txt file:

.. code-block::  shell-session

    -e git+https://github.com/RevSquare/django-brightcove#egg=django-brightcove

And run:

.. code-block::  shell-session

    pip install -r requirements.txt

*****
Setup
*****

Before starting, you will need a Brightcove API token in order to connect to brightcove: http://docs.brightcove.com/en/video-cloud/media/references/reference.html

The first step is to add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'django-brightcove'
        ...
    )

The you will need to declare the loaders you want to add in your settings.py file

.. code-block::  python

    BRIGHTCOVE_TOKEN = 'YOUR_TOKEN..'

Finally you will need to add the django-brightcove urls to your Root URLCONF

.. code-block::  python

    urlpatterns = patterns('',
        ...

        (r'^django_brightcove', include('django_brightcove.urls')),
        ...
    )  

    
    
******************************
Add a bricove video to a model
******************************

Simply add the Brightove field manager to it.

.. code-block::  python

    from django.db import models
    from django_brightcove.managers import BrightcoveManager


    class MyModel(models.Model):
        brightcove = BrightcoveManager()
