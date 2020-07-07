#!/bin/sh

echo "Docker container has been started"
python manage.py runserver 0.0.0.0:8000

# Setup a cron schedule
echo "20 4 * * * /runtask.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f