# Currency Exchange API

This is a API built with FastAPI and SQLAlchemy for managing currency exchange rates.

## Features

- **Update Exchange Rates**: Endpoint to fetch the latest exchange rates from an external API and update the database.
- **Last Update**: Endpoint to retrieve the timestamp of the last update of exchange rates in the database.
- **Currency Conversion**: Endpoint to convert an amount from one currency to another based on the latest exchange rates.

## Endpoints

### Update Exchange Rates

- **URL**: `/update_rates`
- **Method**: `GET`
- **Description**: Fetches the latest exchange rates from an external API and updates the database.
- **Response**: Returns a JSON message indicating the success of the update.

### Last Update

- **URL**: `/last_update`
- **Method**: `GET`
- **Description**: Retrieves the timestamp of the last update of exchange rates in the database.
- **Response**: Returns a JSON object containing the timestamp of the last update.

### Currency Conversion

- **URL**: `/convert`
- **Method**: `POST`
- **Description**: Converts an amount from one currency to another based on the latest exchange rates.
- **Request Body**:
  - `source_currency`: The currency code of the source currency.
  - `target_currency`: The currency code of the target currency.
  - `amount`: The amount to convert.
- **Response**: Returns a JSON object containing the converted amount.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Build the Docker containers using `docker-compose -f docker-compose.yml up --build -d`.
4. Once the containers are running, the API will be accessible at `http://localhost:8000`.

## Dependencies

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for Python.
- httpx: Asynchronous HTTP client for making requests to external APIs.
- pydantic: Data validation and settings management using Python type annotations.
- PostgreSQL: Database management system for storing currency exchange data.

## Environment Variables

- `DATABASE_URL`: Connection URL for the PostgreSQL database.

## Usage

1. Use the `/update_rates` endpoint to fetch and update the latest exchange rates.
2. Convert currency using the `/convert` endpoint by providing the source currency, target currency, and amount.
3. Retrieve the timestamp of the last update using the `/last_update` endpoint.

#### Contacts
telegram - @tim31560
