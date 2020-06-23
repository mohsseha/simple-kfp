#!/bin/bash

set -e #ensures that the script blows up if we face an error. Be careful http://mywiki.wooledge.org/BashFAQ/105 

docker_user='mohsseha'
GIT_SHA=`git rev-parse HEAD`
CWD=`pwd`

for comp_name in comp_*
do
    export docker_name=$docker_user/$comp_name:$GIT_SHA
    echo building $docker_name
    cd $comp_name
    docker build -t $docker_name --build-arg comp_name=$comp_name  . &&
    docker push docker.io/$docker_name
    cd $CWD
done

