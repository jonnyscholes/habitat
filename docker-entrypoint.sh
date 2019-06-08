#!/bin/sh
set -e

until psql postgres://app_user:changeme@db/app_db -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

exec "$@"
