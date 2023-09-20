from fastapi import FastAPI, Query, Path
from router.product import router as product_router
#from models.product import Product

# Query y Path para validaciones

app=FastAPI()



message = [
    {
        "destinatario": "Andy",
        "texto":"I have been studying:",
        "programs1":'Venv',
        "programs2":'Python',
        "programs3":'uvicorn',
        "programs4":'FastAPI',
        "programa5":'AWS'
    }
] 

'''products =[
    {
        "id":1,
        "name":"pordcut 1",
        "price":20,
        "stock":10
    },
    {
        "id":2,
        "name":"pordcut 2",
        "price":25,
        "stock":5
    }
] '''


@app.get('/')
def message_for_andy():
    return message

app.include_router(product_router)

"""
todo esto se movio para router/product 
y donde decia @app lo cambie por @router
y agrego esta dos linea para agregar el router a la app
from router.product import router as product_router
app.include_router(product_router)
 @app.get('/products')
def get_products():
    return products

#parametro
@app.get('/products/{id}')
def get_products(id:int=Path(gt=0)):
    return list(filter(lambda item: item['id']==id,products))
    
#parametro query
@app.get('/products/')
def get_products_by_stock(stock:int,price:float=Query(gt=0)):
    return list(filter(lambda item: 
                       item['stock']==stock and 
                       item['price']==price
                       ,products))

@app.post('/products')
def create_product(product:Product):
    products.append(product)
    return products

@app.put('/prodcuts/{id}')
def update_product(id:int, product:Product):
    for index, item in enumerate(products):
        if item['id']==id:
            products[index]['name']=product.name
            products[index]['stock']=product.stock
            products[index]['price']=product.price
    return products

@app.delete('/prodcuts/{id}')
def delete_product(id:int):
    for item in products:
        if item['id']==id:
           products.remove(item)
    return products """