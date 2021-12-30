FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install python -y
RUN apt-get install python-pip -y

COPY app.py /home/app.py
COPY requirements.txt /home/requirements.txt
COPY quotes_api /home/quotes_api

RUN pip install -r /home/requirements.txt

ENTRYPOINT FLASK_APP=/home/app.py flask run --host=0.0.0.0