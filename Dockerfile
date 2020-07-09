FROM python:3.8-alpine3.11
#FROM python:3

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app
COPY ./python/my_app.py /app

# run the command
# https://docs.docker.com/engine/reference/builder/#run
#RUN apk update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN which pip
RUN pip --version
RUN python3 --version

ENTRYPOINT ["python"]

CMD ["my_app.py"]
