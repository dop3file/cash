FROM python:3.12

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

COPY cash ./cash

RUN poetry install --without dev

EXPOSE 8001

ENTRYPOINT ["poetry", "run", "python", "-m", "cash.main"]