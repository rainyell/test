
FROM python:3.12.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./functions /code/functions

COPY ./test /code/test

COPY ./app_fast_api.py /code/app_fast_api.py

COPY ./database.db /code/database.db

EXPOSE 8000

CMD ["python", "app_fast_api.py", "--port", "8000"]