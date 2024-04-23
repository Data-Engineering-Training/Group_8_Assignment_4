FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password

COPY ./query.sql /docker-entrypoint-initdb.d/
COPY ./data_frame.csv /docker-entrypoint-initdb.d/
