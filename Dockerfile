FROM python:3.7

RUN apt-get update && apt-get install -y \
  stress \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
