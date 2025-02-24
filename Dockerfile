FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libcairo2-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hoshivision.wsgi:application"]