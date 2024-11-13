from fastapi import FastAPI, Response

app = FastAPI()

# com si fos una BDD
items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, response: Response):
    if item_id not in items:
        response.status_code = 404
        return {"detail": "Item not found"}
    return {"item": items[item_id]}
