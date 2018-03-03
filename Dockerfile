FROM selenium/standalone-chrome

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

RUN mkdir /home/seluser/app/
RUN mkdir /home/seluser/app/DB
RUN mkdir /home/seluser/app/Twitter

ADD requirements.txt /home/seluser/app/requirements.txt
ADD HeatonistMonitor.py /home/seluser/app/HeatonistMonitor.py
ADD DB/create_db.py /home/seluser/app/DB/create_db.py
ADD DB/populate_db.py /home/seluser/app/DB/populate_db.py
ADD Twitter/config.py /home/seluser/Twitter/config.py

WORKDIR /home/seluser/app/

RUN sudo pip3 install -r requirements.txt

CMD ["python3", "./DB/create_db.py"]
CMD ["python3", "./DB/populate_db.py"]
RUN find .
CMD ["python3", "HeatonistMonitor.py"]
