FROM python:3.10-bullseye

RUN apt install -y libssl1.1 libssl-dev libmariadb-dev-compat libmariadb-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY .  /app/

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]