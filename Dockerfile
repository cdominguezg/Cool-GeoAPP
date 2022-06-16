FROM python:3.9-slim


EXPOSE 8000
COPY . .
RUN pip install pipenv
RUN pipenv install
ENV FLASK_APP=app.main:create_app
ENV STAGE=prod
CMD ["pipenv", "run", "start"]

