FROM python:3.8
MAINTAINER Kfp Developer (kfp@domain.com)
ARG comp_name

WORKDIR /workdir
RUN mkdir /workdir/$comp_name

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY *.py $comp_name/


CMD ["python3"]



