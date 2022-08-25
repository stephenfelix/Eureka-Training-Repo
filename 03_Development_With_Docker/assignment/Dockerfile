# syntax=docker/dockerfile:1
FROM python:3.6-alpine
RUN apk add g++ jpeg-dev zlib-dev libjpeg make python3-tkinter
WORKDIR /workspace/repo
COPY . /workspace/repo
COPY requirements.txt requirements.txt
#RUN apt-get install python3-tk
RUN pip install -r requirements.txt
CMD ["python", "/workspace/repo/program.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
