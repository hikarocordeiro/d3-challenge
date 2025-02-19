FROM python:3-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN ["python3", "-m", "pytest"]

EXPOSE 5000

CMD ["python", "app.py"]
