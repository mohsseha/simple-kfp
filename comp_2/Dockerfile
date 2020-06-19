# needs to have python3 installed
FROM clojure 
MAINTAINER Kfp Developer (kfp@domain.com)
ARG comp_name

RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR /workdir
RUN mkdir /workdir/$comp_name
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY *.py $comp_name/
CMD [ "python3" ]



