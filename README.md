# Project Description
This is a django web app template.

&nbsp;
## Dream Home Developments
A django platform boilerplate for real state web applications. A common marketplace to present properties at their best where you can chose your own dream home. 

## Instractions
<span style="color:#77708a">Note: If you want to work with main environment then skip the second step</span>
+ Clone template
    > ```console
    > $ git clone https://github.com/MIProtick/DreamHome.git
    > $ cd DreamHome
    > ```
+ Create Virtual Environment
    > *Windows*
    > ```console
    > $ python -m venv ./venv
    > $ venv\Scripts\activate.bat
    > ```
    > &nbsp;

    > *Others OS*
    > ```console
    > $ python -m venv ./venv
    > $ source venv/bin/activate
    > ```
    > &nbsp;
+ Run requirements
    > ```console
    > $ pip install -r requirements.txt
    > ```

+ Setup database
  - Install and configure database among 
    *  [PostgreSQL](https://www.postgresql.org/)
    *  [MariaDB](https://mariadb.org/)
    *  [MySQL](https://www.mysql.com/)
    *  [Oracle](https://www.oracle.com/database/)

  - Setup the <span style="color:#77708a">setting.py</span> file as follow
    > ```python
    > # I've used PostgreSQL DB. Change the configuration accourding to your database.
    >DATABASES = {
    >   'default': {
    >       'ENGINE': 'django.db.backends.postgresql',
    >       'NAME': 'your_database_name',
    >       'USER': 'postgres',
    >       'PASSWORD': 'your_password',
    >       'HOST': 'localhost'
    >   }
    >}
    > ```

  - Run the following code
    > ```console
    > $ python manage.py collectstatic
    > $ python manage.py makemigrations
    > $ python manage.py migrate
    > ```

  - Now create a super user for this project
    > ```console
    > $ python manage.py createsuperuser
    > ```
    &ensp;&ensp;&ensp;Provide your *username*, *email*, *password* and voalá

  - Run the server
    > ```console
    > $ python manage.py runserver
    > ```

  <span style="color:#77708a">_Log in to the admin pannel and insert appropriate data for thi application and **Voalá**_ :tada::trophy:</span>


### Author: *MIProtick*
### Project Address: *https://github.com/MIProtick/DreamHome.git*
Prerequisit: *[ `Python3` ]*

