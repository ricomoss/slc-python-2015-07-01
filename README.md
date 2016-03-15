Polymorphism & Handling Dead Services
=====================================

This repository was created to support the presentation given at the Salt Lake City Python Meetup on July 1st, 2015.  You can find the presentation .pdf included in this repository.

The bulk of this repository is an example Python project that provides a few use-cases for how to use interfaces in Python to handle broken services.  Note this example is using Python 3 but should be Python 2.7+ compatible.

Installation
============

To begin you can clone this repository and setup a virtual environment using the following instructions.

Notes:

    The following will assume you are cloning the sourcecode to **~/Projects/slc-python-2015-07-01**.  If you are cloning to a different location, you will need to adjust these instructions accordingly.

    A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/slc-python-2015-07-01.git

2. Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to your **~/.bashrc** or **~/.zshrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv <virtualenv name> -p /usr/bin/python3


7.  Add the following to the end of the file **~/.virtualenvs/\<virtualenv name\>/bin/postactivate**::

        export PYTHONPATH=~/Projects/slc-python-2015-07-01

8.  Activate the virtualenv::

        $ workon <virtualenv name>

9.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (<virtualenv name>)$ pip install -r ~/slc-python-2015-07-01/requirements.pip

10.  You can now run the **main.py** script.::

        (<virtualenv name>)$ python ~/slc-python-2015-07-01/weather/main.py
