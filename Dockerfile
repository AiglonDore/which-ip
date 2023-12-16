FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv venv

ENV PATH="/venv/bin:$PATH"

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000/tcp

CMD ["python", "core/__main__.py"]