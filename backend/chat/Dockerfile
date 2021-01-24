FROM python:3.7.5-slim-buster

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

#CMD [ "chmod", "+x", "/code/entrypoint.sh" ]

