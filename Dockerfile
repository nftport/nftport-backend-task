FROM python:3.8
ENV PYTHONUNBUFFERED 1

ARG DJANGO_SETTINGS_MODULE=nftport_task.config.production
ARG DJANGO_CONFIGURATION=Production

ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
ENV DJANGO_CONFIGURATION=$DJANGO_CONFIGURATION

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - nftport-backend-task.wsgi:application
