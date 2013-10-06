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

    $ pip install -e git+git://github.com/arteria.ch/python-uptimerobot.git#egg=uptimerobot

 


Usage
-----

Use with Python:

.. code-block:: python

    >>> from uptimerobot.uptimerobot import UptimeRobot
    >>> up = UptimeRobot(UPTIME_ROBOT_API_KEY)
    >>> up.addMonitor("arteria Webpage", "https://www.arteria.ch/")
    True


Use in Shell: (success if return value is 0, null)

.. code-block:: bash

    cd /path/to/script/
    chmod 755 uptimerobot.py # if necessary
    ./uptimerobot.py monitorFriendlyName=Risiko monitorURL=http://www.risiko.arteria.ch/de/risk/list/



Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-uptimerobot
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
