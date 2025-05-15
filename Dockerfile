FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

# ติดตั้ง dependencies ที่จำเป็น
RUN apt-get update && apt-get install -y build-essential libpq-dev

# สร้างโฟลเดอร์ใน container
RUN mkdir /app
WORKDIR /app

# คัดลอกไฟล์ requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโปรเจกต์ของคุณ
COPY . /app/

# ติดตั้ง gunicorn
RUN pip install gunicorn
