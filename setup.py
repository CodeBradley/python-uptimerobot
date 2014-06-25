# -*- encoding: utf-8 -*-
"""
Python setup file for the uptimerobot app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
uptimerobot/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html

"""
import os
from setuptools import setup, find_packages
import uptimerobot as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="python-uptimerobot",
    version=app.__version__,
    description="""Uptime Robot http://uptimerobot.com integration for your Python project. 
    There is a Django version (https://github.com/arteria/django-uptimerobot) available containing the Uptime Robot 
    API implementation and the infrastructure stuff used by Djangonauts. """,
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='uptime robot, API, monitoring',
    author='arteria GmbH',
    author_email='admin@arteria.ch',
    url="https://github.com/arteria/python-uptimerobot",
    packages=find_packages(),
    include_package_data=True,
)
