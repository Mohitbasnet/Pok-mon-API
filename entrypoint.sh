#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Load Pokémon data
python manage.py load_pokemon

exec "$@"
