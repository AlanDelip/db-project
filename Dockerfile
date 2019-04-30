# Basic flask container
FROM fanoftal2/flask-crud-base:1

WORKDIR /home/app/

EXPOSE 5000

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir click flask_restful flask_cors
CMD ["python3", "server.py"]