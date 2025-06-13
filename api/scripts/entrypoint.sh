#!/bin/bash

env_file=".env"

set -a
source "$env_file"
set +a

# === Instalación de dependencias ===
if [[ "$ENV" == "development" ]]; then
  echo -e "\033[1;36mInstalando dependencias...\033[0m"
  pip install -r requirements.txt

  # === Pruebas ===
  echo ""
  echo -e "\033[1;36mPruebas de código...\033[0m"
  pytest
fi

# # === Inicio del servidor ===
echo ""
echo -e "\033[1;36mIniciando servidor...\033[0m"

if [[ "$ENV" == "development" ]]; then
  uvicorn main:app --host 0.0.0.0 --port 80 --reload
else
  uvicorn main:app --host 0.0.0.0 --port 80
fi
