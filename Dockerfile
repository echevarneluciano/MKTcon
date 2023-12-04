FROM python:3.12.0-alpine3.18

WORKDIR /app

COPY  ./requirements.txt ./

RUN pip install --upgrade pip

RUN apk add --no-cache gcc musl-dev mysql-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]