from fastapi import APIRouter
from model.category import Category
from schema import category as schema
from typing import List


router = APIRouter()


@router.get('/', response_model=List[schema.Category])
def get_categories():
    return list(Category.select())

@router.post('/create', response_model=schema.Category)
def create_category(category: schema.CategoryCreate):
    return Category.create(**category.dict())