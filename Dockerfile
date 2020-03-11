FROM python:3.7-alpine
# The alpine image is a lighter weight version of python.

# Prevents python from buffering output.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# We do this user thing for security purposes.
# If we didn't create this user, our app would be run by root, which is dangerous.
RUN adduser -D user
USER user
