# pull official base image
FROM python:3.7-buster

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
ENV CONFIG_ROOT /config

# set work directory
RUN mkdir ${CONFIG_ROOT}
RUN mkdir ${APP_ROOT}

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ${CONFIG_ROOT}/
RUN pip install -r ${CONFIG_ROOT}/requirements.txt
RUN apt-get update && apt-get install -y cron

# copy project
WORKDIR ${APP_ROOT}
COPY . .
#run application
RUN chmod +x ./entrypoint.sh && chmod +x ./runtask.sh
ENTRYPOINT ["./entrypoint.sh"]