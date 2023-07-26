# Use the official Python image as the base image
FROM python:3.9 as base

# Set the default value for RUN_ENV if not provided
ARG RUN_ENV=production

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
RUN chmod +x /app/scripts/build.sh
RUN /app/scripts/build.sh

RUN chmod +x /app/scripts/entry_point.sh
ENTRYPOINT ["poetry", "run", "bash", "-c", "/app/scripts/entry_point.sh"]