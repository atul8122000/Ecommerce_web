# Ecommerce Application Backend

This is a sample backend application built using FastAPI and Python. It serves as a basic implementation for an ecommerce application similar to Flipkart/Amazon. The application provides several APIs to manage products and orders.

## Requirements

- Python 3
- FastAPI
- Pydantic
- pymongo
- json

## Installation

Install the required dependencies using pip:
- pip install fastapi
- pip install uvicorn
- pip install pydantic
- pip install pymongo

# Usage
1. Start the FastAPI server by running the following command in the project directory:
```bash
uvicorn main:app --reload
or 
python -m uvicorn main:app --reload
```
2. The server will start running on http://localhost:8000.
3. Use the API endpoints to interact with the application.



## API Endpoints

The application provides the following API endpoints:

- **List all available products**
    - `GET /products`
    ```
    GET http://localhost:8000/products
    ```
    - Returns a list of all available products in the system.

- **Create a new order**
    - `POST /orders`


  ```
  POST http://localhost:8000/orders

  Request Body:
  {
      "timestamp": "2023-07-07T10:00:00",
      "items": [
          {
              "product_id": 1,
              "bought_quantity": 2
          },
          {
              "product_id": 2,
              "bought_quantity": 1
          }
      ],
      "total_amount": 1999.97,
      "user_address": {
          "city": "Bhopa",
          "country": "India",
          "zip_code": "453120"
      }
  }
  ```
    - Creates a new order with the provided details, including timestamp, items, total amount, and user address.

- **Fetch all orders**
    - `GET /orders`
    ```
    GET http://localhost:8000/orders?limit=10&offset=0
    ```

    - Retrieves all orders from the system, with optional pagination support using the `limit` and `offset` query parameters.

- **Fetch a single order**
    - `GET /orders/{order_id}`
    ```
    GET http://localhost:8000/orders/{order_id}
    ``````
    - Retrieves a specific order based on the provided `order_id`.

- **Update product quantity**
    - `PUT /products/{product_id}`
    ```
    PUT http://localhost:8000/products/{product_id}

    Request Body:
    {
        "quantity": 15
    }
    ```
    - Updates the available quantity for a specific product based on the provided `product_id`.

## Data Models

The application uses the following data models:

- `Product`: Represents a product with attributes like name, price, and quantity.
- `Item`: Represents an item in an order, including the product ID and the bought quantity.
- `Address`: Represents a user's address with attributes like city, country, and zip code.
- `Order`: Represents an order with attributes like timestamp, items, total amount, and user address.

## Contributing

Contributions to improve and enhance the application are welcome.
