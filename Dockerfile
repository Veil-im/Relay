# Start of Selection
FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip install uv

RUN uv pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# End of Selection