from fastapi import FastAPI
app=FastAPI()

@app.get("/profile/{id}")
def showprofile(id:int):
    return {"ID":id}

@app.get("/name/{name}")
def showname(name):
    return {"NAME":name}

@app.get("/square/{id}")
def getidsquare(id:int):
    return {"square":id*id}
