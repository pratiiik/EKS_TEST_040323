FROM python:alpine3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN touch production.log

copy . .

ENTRYPOINT [ "python3", "./prog_long_app.py"]
