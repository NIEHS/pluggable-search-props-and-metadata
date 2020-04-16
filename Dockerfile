FROM python:3-alpine

RUN apk add build-base
RUN apk add libffi-dev
RUN apk add libressl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]


# docker build -t gitlab.niehs.nih.gov:4567/conwaymc/datacommons/projects-and-samples:dev | prod .
# docker run -p 8082:8080 gitlab.niehs.nih.gov:4567/conwaymc/datacommons/projects-and-samples:dev | prod