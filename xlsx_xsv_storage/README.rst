xlsx-xsv-storage
================

Service storage files with pattern *.xlsx|*.csv in DB. This file have to be without pk (primary id) or id columns.
For example if file name is 'fruits2'. With same name will be crete table in DB.
Than read information from this file.
    * get all columns name
    * get types for each columns ( If type from one of cell will be different from each other cell from the same column, that will be type is 'text' )
    * get all rows


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy xlsx_xsv_storage

Test coverage
^^^^^^^^^^^^^

To run the tests without docker

    $ coverage run -m pytest

To run the tests without docker

    $ docker-compose -f local.yml run django coverage run -m pytest


Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

For project build need to run docker-compose like this docker-compose -f local.yml up --build

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



