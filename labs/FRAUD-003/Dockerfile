# Laboratory-only image; no customer data or production connections.
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY app.py dashboard.html dashboard.js /app/
RUN useradd --system --uid 10001 --home /app lab && mkdir -p /data && chown -R lab:lab /data /app
USER lab
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
