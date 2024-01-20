FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv venv

ENV PATH="/venv/bin:$PATH"

RUN pip install -r requirements.txt

COPY . .

ENV LOG_DIR="/var/log/app"

VOLUME [ "$LOG_DIR" ]

EXPOSE 5000/tcp

CMD ["python", "app.py"]