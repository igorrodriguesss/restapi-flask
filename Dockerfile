FROM python:3.10.12-alpine3.18

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py .
COPY config.py . 
COPY application application

CMD [ "python", "wsgi.py" ]