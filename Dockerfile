FROM python:3.12
LABEL authors="9783e6"
LABEL version="1.0"
LABEL description="Simple discord bot which suggests what you can build next."


ADD main.py .
ADD config.py .
ADD requirements.txt .
ADD cogs ./cogs
ADD utils ./utils

RUN pip install -r requirements.txt

ENV TOKEN="not set"
ENV InstanceRanBy="not specified"

CMD ["python", "./main.py"]
