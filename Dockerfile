FROM python:3.6

RUN apt-get -yqq update && \
    apt-get -yqq install unzip && \
    apt-get -yqq install python3-bs4 && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
WORKDIR app
COPY * /app/
RUN pip install -r requirements.txt
CMD ./start.sh