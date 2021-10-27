# pull official base image
FROM python:3.7.12-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat && apt-get -y install cron

# Copy vaccine-cron file to the cron.d directory
COPY vaccine-cron /etc/cron.d/vaccine-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/vaccine-cron

# Apply cron job
RUN crontab /etc/cron.d/vaccine-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]