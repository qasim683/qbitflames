FROM python:3

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils

RUN apt-get install -y libapache2-mod-wsgi 
RUN apt-get install -y git

WORKDIR /var/www/html
RUN git clone https://github.com/qasim683/django_apache2.git && cd django_apache2
#RUN rm -f /var/www/django_apache2/qbit/wsgi.py
#COPY ./wsgi.py /var/www/django_apache2/qbit/
WORKDIR /var/www/html/django_apache2
RUN pip3 install -r requirements.txt
RUN pip install django ptvsd


RUN rm -f /etc/apache2/sites-available/000-default.conf
COPY ./000-default.conf /etc/apache2/sites-available/


RUN mkdir /var/www/logs/
EXPOSE 80


CMD ["apache2ctl","-D","FOREGROUND"]


