Step 1 — Install MySQL
We’ll be using MySQL as our database. You may alternately wish to use another database or already have a database installed, in which case you should skip this step.

To install MySQL to an Ubuntu 20.04 server, type the following:

	$ sudo apt install mysql-server

You should receive the following output:

Output
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-05-07 20:22:51 UTC; 3min 7s ago
   Main PID: 2052 (mysqld)
     Status: "Server is operational"
      Tasks: 38 (limit: 1137)
     Memory: 317.4M
     CGroup: /system.slice/mysql.service
             └─2052 /usr/sbin/mysqld
Ensure that the feedback you receive states that your MySQL server is active. Once that is true, you can continue this tutorial.

Step 2 — Create the Initial Django Project Skeleton
In order to lay the groundwork for our application, we need to generate the project skeleton using the django-admin command. This generated project will be the foundation of our blog app.

Navigate to the directory where you would like to build your blog app. Within that directory, we’ll create a specific directory to build the app. Call the directory something meaningful for the app you are building. As an example, we’ll call ours my_blog_app.

	$ mkdir my_blog_app
Now, navigate to the newly created directory:

	$ cd my_blog_app
Next, move into the programming environment you would like to use for working in Django. You can use an existing one, or create a new one. We’ll call ours env, but you should use a name that is meaningful to you. Once it’s created you can activate it.

	$ python3 -m venv env
	$ . env/bin/activate
Now install Django into this environment if you have not done so already:

	$ pip install django
While in the my_blog_app directory, we will generate a project by running the following command:

	$ django-admin startproject blog
Verify that it worked by navigating to the blog/ directory:

	$ cd blog
The blog/ directory should have been created in the current directory, ~/my_blog_app/, after running the previous django-admin command.

Run ls to verify that the necessary items were created. There should be a blog directory and a manage.py file:

Output
blog manage.py
Now that you’ve created a project directory containing the initial start of your blog application, we can continue on to the next step.

Step 3 — Edit Settings
Since we’ve generated the skeleton project, we now have a settings.py file.

In order for our blog to have the correct time associated with our area, we will edit the settings.py file so that it will be using your current time zone. You can use this list of time zones as a reference. For our example, we will be using America/New_York time.

We want to edit the file, so let’s open the path to the file with our text editor of choice. Here, we’ll use nano.

nano ~/my_blog_app/blog/blog/settings.py
Since we are editing the TIME_ZONE field, we’ll navigate to the bottom section of the file, similar to below.

settings.py
...
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
...
We are going to modify the TIME_ZONE line so that it is set to your current time zone. We will be using the time zone for New York in this example:

settings.py
...
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True
...
Let’s keep the file open because we need to add a path for our static files. The files that get served from your Django web application are referred to as static files. This could include any necessary files to render the complete web page, including JavaScript, CSS, and images.

Go to the end of the settings.py file and add STATIC_ROOT as shown below:

settings.py
...
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
Now that we’ve added the time zone and the path for static files, we should next add our IP to the list of allowed hosts. Navigate to the line of the settings.py file where it says ALLOWED_HOSTS, it’ll be towards the top of the settings.py file.

settings.py
...
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['your server IP address']

# Application definition
...
Add your server’s IP address between the square brackets and single quotes.

Once you are satisfied with the changes you have made, save the file. If you are in nano, you can do so by pressing CTRL + X and then y to confirm changes.

You’ve successfully edited your settings.py file so that the proper time zone has been configured. You’ve also added the path for your static files, and set your ip address to be an ALLOWED_HOST for your application.

Finally, let’s create an administrative user so that you can use the Djano admin interface. Let’s do this with the createsuperuser command:

	$ python manage.py createsuperuser
You will be prompted for a username, an email address, and a password for your user.

At this point we can go on to setting up our database connection.

Step 4 — Install MySQL Database Connector
In order to use MySQL with our project, we will need a Python 3 database connector library compatible with Django. So, we will install the database connector, mysqlclient, which is a forked version of MySQLdb.

First ensure that you have python3-dev installed. You can install python3-dev by running the following command:

	$ sudo apt install python3-dev 
We can now install the necessary Python and MySQL development headers and libraries:

sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
Press y and ENTER to accept the installation.

Once the installation is complete, we will use pip3 to install the mysqlclient library from PyPi. Since our version of pip points to pip3, we can just use pip.

	$pip install mysqlclient
You will receive output similar to this, verifying that it is installing properly:

successfully installed mysqlclient
...
Successfully installed mysqlclient-1.4.6
We have now successfully installed the MySQL client using the PyPi mysqlclient connector library.

Step 5 — Create the Database
Now that the skeleton of your Django application has been set up and mysqlclient and mysql-server have been installed, we will to need to configure your Django backend for MySQL compatibility.

Log in via the MySQL root with the following command:

	$ sudo mysql -u root
We’ll know we are in the MySQL server when our prompt changes:


Let’s inspect the current databases with the following command:

SHOW DATABASES;
You’ll see output similar to the following, assuming that you haven’t created any databases yet:

Output
+--------------------+
| Database          |
+--------------------+
| information_schema |
| mysql             |
| performance_schema |
| sys               |
+--------------------+
4 rows in set (0.00 sec)
Note: If you get an error while trying to connect, verify that your password is correct and that you’ve properly installed MySQL. Otherwise revisit the tutorial on how to install and configure MySQL.

By default, you will have 4 databases already created, information_schema, MySQL, performance_schema and sys. We won’t need to touch these, as they contain information important for the MySQL server itself.

Now, that you’ve successfully logged into your MySQL server, we will create the initial database that will hold the data for our blog.

To create a database in MySQL run the following command, using a meaningful name for your database:

CREATE DATABASE blog_data;
Upon successful creation of the database, you will see the following output:

Output
Query OK, 1 row affected (0.00 sec)
Note: If you see the following output:

database creation failed
ERROR 1007 (HY000): Can't create database blog_data; database exists
Then, as the error states, a database of the name blog_data already exists.

And if you see the following MySQL error, it means there’s a MySQL syntax error. Verify that you’ve entered the command exactly as shown in this tutorial.

database creation failed
ERROR 1064 (42000): You have an error in your SQL syntax;
Next, verify that the database is now listed in your list of available databases:

SHOW DATABASES;
You should see that the blog_data database is among the databases included in the output:

output
+--------------------+
| Database          |
+--------------------+
| information_schema |
| blog_data         |
| mysql                 |
| performance_schema |
| sys               |
+--------------------+
5 rows in set (0.00 sec)
Next, we are going to create a separate MySQL user account that we will use exclusively to operate our new database. Creating specific databases and accounts can support us from a management and security standpoint. We will use the name djangouser in this guide, but feel free to use whatever name is relevant for you.

We are going to create this account, set a password, and grant access to the database we created. We can do this by typing the following command. Remember to choose a strong password here for your database user where we have password:

CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
Next, let the database know that our djangouser should have complete access to the database we set up:

GRANT ALL ON blog_data.* TO 'djangouser'@'%';
You now have a database and user account, each made specifically for Django. We need to flush the privileges so that the current instance of MySQL knows about the recent changes we’ve made:

FLUSH PRIVILEGES;
With that complete, you can exit MySQL server by typing EXIT; or pressing CTRL + D.

Step 6 — Add the MySQL Database Connection to your Application
Finally, we will be adding the database connection credentials to your Django application.

Note: It is important to remember that connection settings, according to the Django documentation, are used in the following order:
- OPTIONS
- NAME, USER, PASSWORD, HOST, PORT
- MySQL option files.

Let’s make the changes needed to connect your Django blog app to MySQL.

Navigate to the settings.py file and replace the current DATABASES lines with the following. We will configure your database dictionary so that it knows to use MySQL as your database backend and from what file to read your database connection credentials.

nano ~/my_blog_app/blog/blog/settings.py
Delete the lines that are there and replace it with the following, being sure to keep the right number of curly braces.

settings.py
...
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
...
Save and close the file.

Next, let’s edit the config file so that it has your MySQL credentials. Use nano as sudo to edit the file and add the following information:

sudo nano /etc/mysql/my.cnf
Add the following lines and include your relevant information.

my.cnf
...
[client]
database = blog_data
user = djangouser
password = your_actual_password
default-character-set = utf8
You’ll notice that utf8 is set as the default encoding, this is a common way to encode unicode data in MySQL. When you are sure that your details are correct, save and close the file.

Once the file has been edited, we need to restart MySQL for the changes to take effect.

	$ sudo systemctl daemon-reload
	$ sudo systemctl restart mysql
