FROM selenium/standalone-chrome

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

RUN mkdir /home/seluser/app/

ADD requirements.txt /home/seluser/app/requirements.txt
ADD HeatonistMonitor.py /home/seluser/app/HeatonistMonitor.py
ADD DB/create_db.py /home/seluser/app/create_db.py
ADD DB/populate_db.py /home/seluser/app/populate_db.py

WORKDIR /home/seluser/app/

RUN sudo pip3 install -r requirements.txt

CMD ["python3", "create_db.py"]
CMD ["python3", "populate_db.py"]
ADD DB/heatonist_monitor.db /home/seluser/app/DB/heatonist_monitor.db
CMD ["python3", "HeatonistMonitor.py"]
