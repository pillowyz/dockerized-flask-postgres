# Dockerized Web App with Flask and PostgreSQL

A simple multi-container web application built with **Flask** and **PostgreSQL**, containerized using **Docker** and orchestrated with **Docker Compose**. The app demonstrates a basic CRUD interface with persistent storage.

## Features

- Flask web application backend
- PostgreSQL database with persistent storage
- Add users via a web interface
- Dockerized and ready to run locally
- Multi-container architecture using Docker Compose

## Tech Stack

- **Backend:** Python 3, Flask  
- **Database:** PostgreSQL  
- **Containerization:** Docker, Docker Compose  
- **Persistence:** Docker volumes

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

### Running Locally

1. Clone the repository:

```bash
git clone https://github.com/pillowyz/dockerized-webapp-postgres.git
cd dockerized-webapp-postgres
```
2. Build the Docker images:

```bash
docker compose build
```
3. Start the containers:

```bash
docker compose up -d
```

4. Open your browser and go to:
```bash
http://localhost:8080
```

5. To stop the containers
```bash
docker compose down
```
