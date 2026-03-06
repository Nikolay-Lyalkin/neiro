set -e

cd /app

poetry run alembic upgrade head

exec "$@"