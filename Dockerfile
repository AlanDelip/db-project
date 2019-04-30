# Basic flask container
FROM fanoftal2/flask-crud-base:1

WORKDIR /home/app/

EXPOSE 8080

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir flask_cors flask_restful click
CMD ["python3", "server.py"]