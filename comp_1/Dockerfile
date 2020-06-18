FROM python:3.8
MAINTAINER Kfp Developer (kfp@domain.com)
ARG comp_name

WORKDIR /workdir
WORKDIR /workdir/$comp_name
COPY requirements.txt .
COPY __init__.py $comp_name


RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python3"]



