# base image
FROM registry.cn-beijing.aliyuncs.com/biyao/public:py310-v3 AS base

WORKDIR /app/api

# Install Poetry
ENV POETRY_VERSION=2.1
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Configure Poetry
ENV POETRY_CACHE_DIR=/tmp/poetry_cache
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_REQUESTS_TIMEOUT=60

FROM base AS packages

# Install Python dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --sync --no-cache --no-root

# production stage
FROM base AS production

RUN apt-get update && apt-get install -y --no-install-recommends curl nodejs

EXPOSE 8000

# set timezone
ENV TZ=UTC

WORKDIR /app/api

# Copy Python environment and packages
ENV VIRTUAL_ENV=/app/api/.venv
COPY --from=packages ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# Copy source code
COPY . /app/api