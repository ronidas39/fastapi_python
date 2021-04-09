from fastapi import FastAPI
app=FastAPI()
@app.get("/getname/{name}")
def show(name):
    return {"NAME":name}