FROM debian:latest

RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip install -U pip

RUN cd /

RUN git clone https://github.com/Kinshu0410

RUN cd Soojh

WORKDIR /Soojh

RUN pip3 install -U-r requirements.txt

CMD python3 PROCFILE
