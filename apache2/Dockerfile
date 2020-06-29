FROM ubuntu

RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install django ptvsd
RUN apt-get install -y git
WORKDIR /var/www/
RUN git clone https://github.com/qasim683/django_apache2.git && cd django_apache2
RUN pip install -r requirements.txt



RUN rm -f /etc/apache2/sites-available/000-default.conf
COPY ./000-default.conf /etc/apache2/sites-available/
COPY ./apache2.conf /etc/apache2/

RUN mkdir /var/www/logs/
EXPOSE 80


CMD ["apache2ctl","-D","FOREGROUND"]


