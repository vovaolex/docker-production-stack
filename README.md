# Docker Production Stack

A simple production-style Docker project using:

- FastAPI
- PostgreSQL
- Nginx
- Docker Compose
- Health checks
- Environment variables

## Architecture

Browser → Nginx → FastAPI → PostgreSQL

## Features

- FastAPI application running in Docker
- PostgreSQL database with persistent volume
- Nginx reverse proxy
- Docker Compose orchestration
- Database health check
- Environment variables stored in `.env`
- `.env.example` for safe configuration sharing

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