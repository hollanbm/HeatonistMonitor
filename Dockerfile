FROM selenium/standalone-chrome

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

RUN mkdir /home/seluser/app/

ADD requirements.txt /home/seluser/app/requirements.txt
ADD HeatonistMonitor.py /home/seluser/app/HeatonistMonitor.py

WORKDIR /home/seluser/app/

RUN sudo pip3 install --upgrade pip
RUN sudo pip3 install -r requirements.txt

CMD ["python3", "HeatonistMonitor.py"]
