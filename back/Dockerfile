FROM jjanzic/docker-python3-opencv
WORKDIR /argos

COPY requirements.txt /argos/requirements.txt
COPY config.yaml /argos/config.yaml
COPY setup.py /argos/setup.py
COPY argos /argos/argos

RUN pip install -r requirements.txt
RUN pip install .

COPY app.py /argos/app.py

CMD ["python", "app.py"]