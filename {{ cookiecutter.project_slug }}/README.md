# The {{ cookiecutter.project_name }} Project

{% if cookiecutter.project_short_description %}{{ cookiecutter.project_short_description }}{% endif %}

## Prepare environment

### Create a virtual environment

```bash
pyenv virtualenv {{ cookiecutter.project_slug }}
pyenv shell {{ cookiecutter.project_slug }}

# or

python -m venv venv
source venv/bin/activate
```

### Install poetry

- poetry is used for easily managing dependency packages

```bash
pip install poetry
```

### Install dependency packages

```bash
poetry install

# for development
poetry install --dev
```

### Create Database

If using sqlite, you can pass this step.
This guide intends to help create PostgreSQL db

```sql
DROP DATABASE IF EXISTS {{ cookiecutter.project_slug }};

CREATE DATABASE {{ cookiecutter.project_slug }};

CREATE ROLE {{ cookiecutter.project_slug }} WITH LOGIN PASSWORD 'password';
ALTER DATABASE {{ cookiecutter.project_slug }} OWNER TO {{ cookiecutter.project_slug }};
```

### Create environment file

``` bash
cp .env.tpl .env

# Update the environment varables as needed
```

### Run migrate to init database for the app

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

### Install pre-commit

```bash
# cd <TO REPO's root directory>
pre-commit install
```

### Run mypy for checking type annotations

```bash
mypy --ignore-missing-imports
```

### Install redis if needed

```bash
# For Ubuntu
## Install redis
sudo apt-get install redis-server
## Start service
sudo service redis-server

# For Mac
## Install redis
brew install redis
## Start service
brew services start redis
```

{% if cookiecutter.use_celery == "y" %}
## Run celery

```bash
ENVIRONMENT=local celery -A {{ cookiecutter.project_slug }}.celery_tasks worker -l info -Q default
ENVIRONMENT=local celery -A {{ cookiecutter.project_slug }}.celery_tasks beat -l info
```

## Run flower to easily manage celery in browsers

```bash
# Run flower to manage celery
ENVIRONMENT=local celery -A {{ cookiecutter.project_slug }}.celery_tasks flower
```

Then navigate to http://localhost:5555/
{% endif -%}
