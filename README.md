# Pokémon API Project

This project serves a list of Pokémon with their names, images, and types through a RESTful API built with Django and Django REST Framework.

## Project Overview

The Pokémon API project allows users to:

- Retrieve a list of Pokémon with details including name, image, and type.
- Filter Pokémon by name and type using query parameters.

## Setup Instructions

### Prerequisites

To run this project locally, ensure you have the following installed:

- Docker
- Docker Desktop

### Steps to Run the Project

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Mohitbasnet/Pok-mon-API.git
   cd Pok-mon-API
2. **Create a .env**:
    ```sh
   DB_NAME=your_database_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=your_hostname
   DB_PORT=your_portname

3. **Build and start Docker containers**:
   ```sh
   docker-compose up --build

4. **Access the API**:
   Open your web browser and go to https://localhost:8000/api/v1/pokemons/ to view the list of Pokémon.

### Docker Configuration
* The project is containerized using Docker, ensuring consistent development and deployment environments.
* PostgreSQL database is initialized and Pokémon data is loaded automatically on startup.
* The Django application runs on port 8000 and connects to PostgreSQL database service named db.
   
