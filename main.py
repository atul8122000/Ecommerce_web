from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import json_util
import json

app = FastAPI()

client = MongoClient('mongodb+srv:')
db = client['flipkart']
collection = db['data']
products = list(collection.find())

products = json.loads(json_util.dumps(products))

orders = []
order_id = 1

class Product(BaseModel):
    name: str
    discount: str

class Item(BaseModel):
    product_id: int
    bought_quantity: int

class Address(BaseModel):
    city: str
    country: str
    zip_code: str

class Order(BaseModel):
    timestamp: str
    items: List[Item]
    total_amount: float
    user_address: Address

@app.get("/")
def well():
    cosmocloud= "wellcome to cosmocloud"
    return cosmocloud

@app.get("/products")
def get_products():
    return products

@app.post("/orders")
def create_order(order: Order):
    global order_id
    order_dict = order.dict()
    order_dict["id"] = order_id
    orders.append(order_dict)
    order_id += 1
    return order_dict

@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    return orders[offset : offset + limit]

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/products/{product_id}")
def update_product(product_id: int, quantity: int):
    for product in products:
        if product["id"] == product_id:
            product["quantity"] = quantity
            return product
    raise HTTPException(status_code=404, detail="Product not found")
