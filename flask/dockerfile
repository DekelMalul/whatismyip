FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY app .

RUN addgroup --system --gid 1001 flask &&\
    adduser --system flask -u 1001 -G flask &&\
    chown -R flask: /app && pip install -r /app/requierments.txt 

USER flask 

EXPOSE 5000

CMD ["python3","wsgi.py"]