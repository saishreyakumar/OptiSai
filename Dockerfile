

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=backend.api.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=10000

EXPOSE 10000

CMD ["flask", "run"]
