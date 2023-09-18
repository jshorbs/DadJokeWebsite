FROM python:3.10.6-slim
ENV PYTHONBUFFERED=1
WORKDIR /backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
