# LAB ONLY — not a production-ready payment or antifraud system.
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
 && useradd --uid 10001 --create-home lab \
 && mkdir -p /data && chown 10001:10001 /data
COPY app.py ./app.py
USER 10001
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
