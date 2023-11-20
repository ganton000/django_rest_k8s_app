# linux
FROM python:3.11-slim

# disable automatic check for pip updates
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# python will not generate .pyc files
ENV PYTHONDONTWRITEBYTEVODE 1
# console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml entrypoint.sh ./

## set up virtual env && install deps
RUN python3 -m venv /opt/venv && \
	/opt/venv/bin/pip install pip --upgrade && \
	/opt/venv/bin/pip install poetry && \
	/opt/venv/bin/poetry install --no-root && \
	chmod +x entrypoint.sh

COPY . .

CMD ["/app/entrypoint.sh"]
