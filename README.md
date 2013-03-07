MapCampus
=========

MapCampus is a web application that visualizes the mapping data collected by the 
University of Illinois Geographic Information Systems club. Built with a combination
of Django, NetworkX, and Tastypie on the backend, and AngularJS and Bootstrap on the
frontend.

## Building MapCampus

1. Install PostgreSQL
    * Will need psycopg2 to work properly with Django.
  * Read the PostgreSQL tutorials for your OS of choice to initialize your database.

2. Install PostGIS
  * Make sure you install the PostGIS extensions in your PostgresSQL database. Topology extensions optional.

3. Setup virtualenv and install requirements.
  * Follow the virtualenv tutorial to setup a new `env` folder in your `mapcampus` directory.
  * Run `pip install -r reqs.txt` to install the required python packages.

4. Run `syncdb` to create tables for all apps not managed by South. 
  * Make sure you create a superuser too, even if the admin interface may be removed at a later date.

5. Run initial schema migrations.
  * Open a terminal and run `python manage.py schemamigration [appname] --initial` for every app you want
    to initialize.

6. Start up Django!

## Authors

**Yihua Lou**

+ [lou13@illinois.edu](lou13@illinois.edu)

**Varun Goel**

+ [goel4@illinois.edu](goel4@illinois.edu)
