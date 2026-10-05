#!/bin/sh
# Deploys the shop container to production.
set -e
PORT=8080
ssh deploy@prod.shop.internal "docker pull shop:latest && docker rm -f shop || true && docker run -d --name shop -p $PORT:80 shop:latest"
curl -fsS "http://prod.shop.internal:$PORT/health"
