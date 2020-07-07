# pull official base image
FROM python:3.7-alpine

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
RUN pip install gunicorn 

# copy project
WORKDIR ${APP_ROOT}
COPY . .
#update database
RUN python manage.py makemigrations api
RUN python manage.py migrate
#run application
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["gunicorn", --"bind", "8000", "siteinfo.wsgi:application" 
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]