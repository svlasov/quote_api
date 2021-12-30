FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

COPY app.py /home/app.py
COPY requirements.txt /home/requirements.txt
COPY quotes_api /home/quotes_api

RUN python3 -m pip install -r /home/requirements.txt

ENTRYPOINT FLASK_APP=/home/app.py python3 -m flask run --host=0.0.0.0
# CMD /bin/bash