FROM python:slim-buster
ADD . /app
WORKDIR /app
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD ["python", "run.py"]
