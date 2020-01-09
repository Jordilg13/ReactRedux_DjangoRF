FROM frolvlad/alpine-python3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev
ADD ./requirements.txt /drf/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /drf/requirements.txt
# EXPOSE 8000
# CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000