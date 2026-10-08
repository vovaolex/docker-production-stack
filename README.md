# Docker Production Stack

A simple production-style Docker project using FastAPI, PostgreSQL, Nginx, and Docker Compose.

## Architecture

```text
Browser
   ↓
Nginx
   ↓
FastAPI
   ↓
PostgreSQL
```

## Features

- FastAPI application running in Docker
- PostgreSQL database with persistent storage
- Nginx reverse proxy
- Docker Compose orchestration
- PostgreSQL health check
- FastAPI waits for the database to become healthy
- Environment variables stored in `.env`
- `.env.example` included for safe configuration sharing

## Project Structure

```text
docker-production-stack/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
├── .env.example
├── .gitignore
├── compose.yaml
└── README.md
```

## Run the Project

Clone the repository:

```bash
git clone https://github.com/vovaolex/docker-production-stack.git
```

Go to the project directory:

```bash
cd docker-production-stack
```

Create the environment file:

```bash
cp .env.example .env
```

Start the containers:

```bash
docker compose up --build
```

Open the application in your browser:

```text
http://localhost
```

Health check endpoint:

```text
http://localhost/health
```

Expected response:

```json
{
  "status": "ok",
  "database": "connected"
}
```

## Stop the Project

```bash
docker compose down
```

## Services

### Nginx

Nginx acts as a reverse proxy.

It exposes the application on port `80` and forwards incoming requests to the FastAPI container.

### FastAPI

FastAPI runs the backend application inside a Docker container.

The application is not exposed directly to the host. It is accessible through Nginx inside the Docker network.

### PostgreSQL

PostgreSQL runs in a separate Docker container.

Database data is stored in a persistent Docker volume so it is not lost when the container is recreated.

## Health Check

PostgreSQL uses Docker's health check functionality with `pg_isready`.

The FastAPI container starts only after PostgreSQL becomes healthy.

Example configuration:

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
  interval: 5s
  timeout: 5s
  retries: 5
```

## Environment Variables

The project uses the following environment variables:

```env
POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=change_me
```

The real `.env` file is excluded from Git using `.gitignore`.

To create it locally:

```bash
cp .env.example .env
```

## Docker Compose Services

The project consists of three services:

```text
nginx
fastapi
postgresql
```

They communicate through the internal Docker network created automatically by Docker Compose.

## Useful Commands

Start the project:

```bash
docker compose up --build
```

Start in detached mode:

```bash
docker compose up -d --build
```

View running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Follow logs in real time:

```bash
docker compose logs -f
```

Stop the containers:

```bash
docker compose down
```

Stop the containers and remove the PostgreSQL volume:

```bash
docker compose down -v
```

## Technologies

- Docker
- Docker Compose
- Python
- FastAPI
- PostgreSQL
- Nginx

## What I Learned

This project demonstrates:

- Building Docker images with a Dockerfile
- Running multiple containers with Docker Compose
- Connecting services using Docker networking
- Using Nginx as a reverse proxy
- Connecting a FastAPI application to PostgreSQL
- Using Docker volumes for persistent storage
- Using environment variables for configuration
- Using health checks and service dependencies
- Separating internal services from externally exposed services