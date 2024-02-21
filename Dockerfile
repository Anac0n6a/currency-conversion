FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]