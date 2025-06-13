SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
env_file="$SCRIPT_DIR/.env"

[[ -f $env_file ]] || cp "$env_file-template" "$env_file"

set -a
source "$env_file"
set +a

if [ ! "$(docker network ls -q -f name=$NETWORK)" ]; then
  docker network create --driver=bridge --subnet=192.150.0.0/16 $NETWORK
fi

# if [ $ENV == 'development' ]; then

IFS=',' read -ra dependencies <<<"${DEPENDENCIES// /}"
for dependency in "${dependencies[@]}"; do
  bash ../$dependency/scripts/installer.sh
done

docker-compose -f $SCRIPT_DIR/docker-compose.yml up -d api
