# syntax=docker/dockerfile:1
# Setup python
FROM tensorflow/tensorflow:latest-gpu-jupyter
RUN apt-get update -y && \
    apt-get install -y apt-utils gfortran musl-dev gcc make g++ libffi-dev libxml2-dev \
    libxml2 libxslt-dev
RUN pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt

# Setup Flask app
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
