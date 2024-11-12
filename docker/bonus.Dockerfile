FROM python:3.10-alpine

WORKDIR /bonus

COPY ./bonus_service /bonus

RUN pip3.10 install -r /bonus/requirements.txt

EXPOSE 8050

CMD ["python3", "app/main.py"]