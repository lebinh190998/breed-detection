# Use the official Python image as the base image
FROM python:3.9 as base

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libxrender1 \
    libjpeg62-turbo \
    fontconfig \
    libxtst6 \
    xfonts-75dpi \
    xfonts-base \
    xz-utils \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev

# Install Poetry
RUN pip install poetry==1.5.1

# Set the working directory in the container
WORKDIR /app

COPY . .

# Install project dependencies
RUN poetry lock && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

RUN poetry add python-multipart

RUN chmod +x /app/scripts/entry_point.sh
ENTRYPOINT ["poetry", "run", "bash", "-c", "/app/scripts/entry_point.sh"]