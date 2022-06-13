FROM python:3.9-slim


EXPOSE 8000
COPY . .
RUN pip install pipenv
RUN pipenv install
RUN pipenv install gunicorn
ENV FLASK_APP=app.main:app
CMD ["pipenv", "run", "start"]

