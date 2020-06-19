#!/bin/bash

docker_user='mohsseha'
GIT_SHA=`git rev-parse HEAD`
export comp_name=`pwd | rev | cut -f1 -d/ |rev`
export docker_name=$docker_user/$comp_name:$GIT_SHA


docker build -t $docker_name --build-arg comp_name=$comp_name  . &&
docker push docker.io/$docker_name
