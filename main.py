from fastapi import FastAPI

app=FastAPI()
@app.get("/sum")
def sum(num1:int,num2:int):
    sum=num1+num2
    return {"sum":sum}