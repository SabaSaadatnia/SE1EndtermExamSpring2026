FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY digital_bank ./digital_bank

CMD ["python", "-m", "digital_bank.app"]