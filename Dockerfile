FROM ubuntu:20.04

ENV IT-RAPS ENV=developpement

WORKDIR /usr/local/src

COPY ai /usr/local/src/ai
COPY data /usr/local/src/data
COPY server /usr/local/src/server
COPY requirements.txt /usr/local/src/requirements.txt
COPY run.sh /usr/local/src/run.sh

RUN sudo apt update && \
  sudo apt install -y build-essential libssl-dev libffi-dev python3-dev 

RUN pip3 install -r requirements.txt

RUN chmod u+x run.sh

EXPOSE 80/tcp
