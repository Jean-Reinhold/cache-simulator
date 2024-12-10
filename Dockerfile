FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

COPY ./requirements ./requirements

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

ENV DEBIAN_FRONTEND=dialog

CMD ["python", "chomp_bytes.py"]