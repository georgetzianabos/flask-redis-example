#!/bin/bash

# Run a local redis server. Download and build if required

if [ -f ./redis-stable/src/redis-server ]; then
    ./redis-stable/src/redis-server
else
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    ./src/redis-server
fi
