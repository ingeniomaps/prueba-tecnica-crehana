#!/bin/bash

env_file=".env"
if [ -f "$env_file" ]; then
  set -a
  source "$env_file"
  set +a
fi

domains=crehana.mifori.com
data_path="./data/certbot"
email="malpisa1@hotmail.com"

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  mkdir -p "$data_path/conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf -o "$data_path/conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem -o "$data_path/conf/ssl-dhparams.pem"
fi

domain_args=$(printf ' -d %s' "${domains[@]}")
domain_args="${domain_args# }" # Remove leading space

docker-compose run --rm --entrypoint " \
  certbot certonly --webroot -w /var/www/certbot \
  --email ${email}
  $domain_args \
  --non-interactive \
  --agree-tos \
  --force-renewal" certbot
