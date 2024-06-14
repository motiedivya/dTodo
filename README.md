
# dTodo

## Overview

dTodo is a comprehensive microservices-based Todo application designed to demonstrate the integration of multiple services using Docker and Kong API Gateway. The application consists of a Todo service, monitoring and logging tools, and API Gateway management.

## Table of Contents

- [dTodo](#dtodo)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Architecture](#architecture)
  - [Services](#services)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Build and Run](#build-and-run)
  - [API Endpoints](#api-endpoints)
  - [Monitoring and Logging](#monitoring-and-logging)
  - [Contributing](#contributing)
  - [License](#license)

## Architecture

The project architecture includes the following components:
- **Todo App**: A microservice handling todo items.
- **Kong API Gateway**: Manages API requests.
- **Consul**: Service discovery.
- **MongoDB**: Database for storing todo items.
- **NSQ**: Messaging service.
- **Prometheus**: Monitoring tool.
- **Grafana**: Dashboard for visualizing metrics.
- **Graylog**: Log management.
- **Elasticsearch**: Search engine.
- **Sonarqube**: Continuous inspection of code quality.

## Services

The project includes the following services:
- **todo-app**: A Python Flask application managing todo items.
- **kong**: Kong API Gateway for managing APIs.
- **consul**: Service discovery.
- **mongodb**: Database service.
- **nsq**: Messaging queue service.
- **prometheus**: Monitoring and alerting toolkit.
- **grafana**: Dashboard for monitoring metrics.
- **graylog**: Log management platform.
- **elasticsearch**: Search and analytics engine.
- **sonarqube**: Continuous code quality inspection.

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose

### Build and Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/dTodo.git
cd dTodo
```

2. **Build the Docker image for the todo-app:**

```bash
docker build -t todo-app-image todo-app/app
```

3. **Start all services using Docker Compose:**

```bash
docker-compose up -d
```

4. **Verify that all services are up and running:**

```bash
docker-compose ps
```

## API Endpoints

- **Todo Service:**

  - **Create Todo Item:**
    ```bash
    curl -i -X POST http://localhost:8010/todo/ \
      -H "accept: application/json" \
      -H "Content-Type: application/json" \
      -d "{\"item\":\"Buy groceries\"}"
    ```

## Monitoring and Logging

- **Prometheus** is available at [http://localhost:9090](http://localhost:9090)
- **Grafana** is available at [http://localhost:3000](http://localhost:3000)
- **Graylog** is available at [http://localhost:9000](http://localhost:9000)
- **Elasticsearch** is available at [http://localhost:9200](http://localhost:9200)
- **Sonarqube** is available at [http://localhost:9001](http://localhost:9001)

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.