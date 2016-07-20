FROM python:2.7
ADD . /code
WORKDIR /code/
RUN apt-get update
RUN apt-get install -y libfreetype6-dev libxft-dev
RUN pip install -r requirements.txt
RUN mysql -uroot -p123456 clasificador < schema.sql
RUN mysql -uroot -p123456 --local_infile=1 clasificador -e "LOAD DATA LOCAL INFILE '/bd.csv' INTO TABLE songs FIELDS TERMINATED BY ','"
EXPOSE 9090
