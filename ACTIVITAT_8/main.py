from fastapi import FastAPI, HTTPException

app = FastAPI()

# com si fos una BDD
items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # excepció per a quan no es troba
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
