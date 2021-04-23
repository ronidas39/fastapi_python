from fastapi import FastAPI
app=FastAPI()
@app.get("/profile/{id}")
def show(id:int):
    return {"ID":id}