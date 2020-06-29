FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils

RUN apt-get install -y libapache2-mod-wsgi 
RUN apt-get install -y git
RUN pip3 install virtualenv
WORKDIR /var/www/
RUN python3 -m venv env
RUN /bin/bash -c "source env/bin/activate"
RUN git clone https://github.com/qasim683/django_apache2.git && cd django_apache2
#RUN rm -f /var/www/django_apache2/qbit/wsgi.py
#COPY ./wsgi.py /var/www/django_apache2/qbit/
WORKDIR /var/www/django_apache2/
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi


RUN rm -f /etc/apache2/sites-available/000-default.conf
COPY ./000-default.conf /etc/apache2/sites-available/
COPY ./apache2.conf /etc/apache2/

RUN mkdir /var/www/logs/
EXPOSE 80


CMD ["apache2ctl","-D","FOREGROUND"]


