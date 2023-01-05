FROM python:3.8.8

RUN pip3 install numpy pandas matplotlib seaborn
RUN pip3 install pytest

WORKDIR /usr/src/app
COPY *.py /usr/src/app/


