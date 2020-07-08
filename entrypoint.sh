#!/bin/bash

# Setup a cron schedule
echo "20 4 * * * /runtask.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f

# setup logging to docker
ln -sf /dev/stdout /code/siteinfo.log

#update database
echo "Updating database..."
python manage.py makemigrations api
python manage.py migrate

echo "Docker container has been started"
python manage.py runserver 0.0.0.0:8000