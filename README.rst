Uptime Robot integration for Python
============

Uptime Robot http://uptimerobot.com integration for your Python project. 
There is a Django version (https://github.com/arteria/django-uptimerobot) available containing the Uptime Robot API 
implementation and the infrastructure stuff used by Djangonauts.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash
	# TODO:
    $ pip install python-uptimerobot

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/arteria/python-uptimerobot.git#egg=uptimerobot

 


Usage
-----

Use with Python:

.. code-block:: python

    >>> from uptimerobot.uptimerobot import UptimeRobot
    >>> up = UptimeRobot(UPTIME_ROBOT_API_KEY)
    >>> up.addMonitor("arteria-webpage", "https://www.arteria.ch/")
    True


Use in Shell: (success if return value is 0, null)

.. code-block:: bash

    cd /path/to/script/
    chmod 755 uptimerobot.py # if necessary
    ./uptimerobot.py monitorFriendlyName=arteria-webpage monitorURL=https://www.arteria.ch/


History
-------

0.0.7

- Python 3.x support
