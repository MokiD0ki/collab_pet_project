from fastapi import FastAPI

app = FastAPI(
    title="CollabTasks (pet)",
    version="0.0.1",
    description="Tiny starter FastAPI app to verify Swagger & project wiring."
)

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item