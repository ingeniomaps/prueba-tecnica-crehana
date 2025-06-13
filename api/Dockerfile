FROM python:3.13-slim

RUN mkdir /code
COPY ./ /code
WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]