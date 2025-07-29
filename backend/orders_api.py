from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["orders"])

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class Order(BaseModel):
    id: int
    items: List[OrderItem]
    total: float
    created_at: datetime

orders_db = []

@router.post("/", response_model=Order)
async def create_order(items: List[OrderItem]):
    order = Order(
        id=len(orders_db) + 1,
        items=items,
        total=sum(item.price * item.quantity for item in items),
        created_at=datetime.now()
    )
    orders_db.append(order)
    return order