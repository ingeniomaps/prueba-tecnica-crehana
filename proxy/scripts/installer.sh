#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
env_file="$SCRIPT_DIR/.env"

[[ -f $env_file ]] || cp "$env_file-template" "$env_file"

set -a
source "$env_file"
set +a

if [ $ENV == 'development' ]; then
  rm -rf $SCRIPT_DIR/data
  mkdir -p $SCRIPT_DIR/data/certbot/conf/live/server
  cp $SCRIPT_DIR/cert/* $SCRIPT_DIR/data/certbot/conf/live/server
fi

if [ ! "$(docker network ls -q -f name=$NETWORK)" ]; then
  docker network create --driver=bridge --subnet=192.150.0.0/16 $NETWORK
fi

docker-compose -f $SCRIPT_DIR/docker-compose.yml up -d proxy
