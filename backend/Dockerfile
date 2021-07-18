FROM python:3.7

WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app/

CMD [ "python3.7", "server.py" ]