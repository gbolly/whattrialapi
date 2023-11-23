FROM python:3.9.18

# Install build dependencies
RUN apk --update --no-cache add \
    build-base \
    linux-headers \
    pcre-dev \
    postgresql-dev

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backend/

# CMD ["sh", "-c", "sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
CMD ["uwsgi", "--module=whattrial.wsgi", "--http=0.0.0.0:80"]

FROM python:3.9.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=quickstart.wsgi
