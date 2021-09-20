FROM kumatea/tensorflow:2.4.1-py38

RUN apt-get update

COPY . .

RUN pip3 install -r ./requirements.txt

EXPOSE 8888

CMD ["run.py"]
ENTRYPOINT ["python3"]