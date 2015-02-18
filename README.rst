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

Before starting, you will need a Brightcove API token in order to connect to brightcove: http://docs.brightcove.com/en/video-cloud/media/guides/managing-media-api-tokens.html

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
    from django_brightcove.fields import BrightcoveField


    class MyModel(models.Model):
        brightcove = BrightcoveField()



*************
Template tags
*************

You can easily insert a video with a built in template tag.

The first step is to list your brightcove player id and key in your settings file.

.. code-block::  python

    BRIGHTCOVE_PLAYER = {
        'default': {
            'PLAYERID': 'a_default_player_id',
            'PLAYERKEY': 'a_default_player_key',
        },
        'single': {
            'PLAYERID': 'another_player_id',
            'PLAYERKEY': 'another_player_key',
        },
    }

Then within your template, simply call for the player tag and pass your video id and eventualy a specific brightcove player type. By default the tag will use the first value in the settings.BRIGHTCOVE_PLAYER dictionary.

.. code-block::  html

    {% load brightcove %}

    <div class="player">{% brightcove_player object.brightcove_id player='single' %}</div>

You can also pass height and width to the template tag, ie:

.. code-block::  html

    {% load brightcove %}

    <div class="player">{% brightcove_player object.brightcove_id width=480 height=270 %}</div>

You will also need to add the Brightcove javascript library

.. code-block::  html

    <script type="text/javascript" src="http://admin.brightcove.com/js/BrightcoveExperiences.js"></script>
