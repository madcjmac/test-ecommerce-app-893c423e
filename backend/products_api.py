from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"])

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str
    category: str
    stock: int

class CartItem(BaseModel):
    product_id: int
    quantity: int

# Mock product database
products_db = [
    Product(id=1, name="Professional Laptop", description="High-performance laptop for professionals", 
            price=1299.99, image="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400", 
            category="Electronics", stock=10),
    Product(id=2, name="Wireless Headphones", description="Premium noise-canceling headphones", 
            price=299.99, image="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
            category="Audio", stock=25)
]

@router.get("/", response_model=List[Product])
async def get_products():
    return products_db

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = next((p for p in products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product