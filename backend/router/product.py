from fastapi import APIRouter, UploadFile
from model.product import Product
from model.image import Image
from schema import product as schema
from typing import List
import base64
from playhouse.shortcuts import model_to_dict

router = APIRouter()

@router.get('/', response_model=List[schema.Product])
def get_product():
    return Product.get_list()



@router.post('/')
def create_product(product: schema.ProductCreate):
    img = Image.create(base64.b64decode(product.image.split(',').pop()))

    product = product.dict()
    product['image'] = [img.id]
    return Product.create(**product)

@router.delete('/{id}')
def delete_product(id: int):
    product = model_to_dict(Product.get_by_id(id))
    images = product['image']

    Product.delete().where(Product.id == product['id']).execute()
    for img in images:
        path = model_to_dict(Image.get_by_id(img))
        path = path['url'].split('/')[-1]
        os.remove(f'image/{path}')
        Image.delete().where(Image.id == img).execute()

    return {'msg': 'Product deleted'}