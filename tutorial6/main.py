from fastapi import FastAPI
app=FastAPI()

@app.get("/profile")
def showprofile(id:int):
    return {"ID":id}

@app.get("/check")
def check(num:int):
    if num >5:
        return {"num is greater than 5"}
    else:
        return {"num is not greater than 5"}

@app.get("/sum")
def sum(num1:int,num2:int):
    return {"SUM":num1+num2}
    