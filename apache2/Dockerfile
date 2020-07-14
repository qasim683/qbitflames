FROM python:3.7

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y apt-utils
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils

RUN apt-get install -y libapache2-mod-wsgi-py3
RUN pip3 install --upgrade pip

RUN apt-get install -y git

WORKDIR /var/www/html

RUN pip3 install virtualenv
RUN virtualenv env
RUN . env/bin/activate

RUN git clone https://github.com/qasim683/django_apache2.git
#RUN rm -f /var/www/django_apache2/qbit/wsgi.py
#COPY ./wsgi.py /var/www/django_apache2/qbit/
RUN mv django_apache2 /var/www/html/qbit
WORKDIR /var/www/html/qbit

RUN /var/www/html/env/bin/pip3 install -r requirements.txt
RUN /var/www/html/env/bin/pip3 install django ptvsd



RUN rm -f /etc/apache2/sites-available/000-default.conf
COPY ./000-default.conf /etc/apache2/sites-available/
RUN a2ensite 000-default.conf

RUN chown -R www-data:www-data .

RUN mkdir /var/www/logs/
RUN rm -f /var/www/html/index.html
EXPOSE 80
 

CMD ["apache2ctl","-D","FOREGROUND"]


