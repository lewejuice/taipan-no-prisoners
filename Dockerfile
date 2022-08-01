FROM python:slim

WORKDIR /app

COPY *.py requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

EXPOSE 10069

CMD ["python", "server.py"]

