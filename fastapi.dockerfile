FROM python:3.10

WORKDIR /code

COPY ./req.txt /code/req.txt
COPY ./env/.env /code/.env

RUN pip install --no-cache-dir --upgrade -r /code/req.txt

COPY ./src /code/src


CMD ["uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port", "8080", "--env-file", "./.env"]
