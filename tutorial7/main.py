from fastapi import FastAPI 
import json

def read_json(file):
    f=open(file)
    data=json.load(f)
    return(data)



app=FastAPI()

@app.get("/users")
def users(isactive:bool):
    if (isactive):
        val="yes"
    else:
        val="no"
    return{"active":val}

@app.get("/user")
def user(id):
    data=read_json("users.json")
    user_data=data["users"]
    name="invalid"

    for row in user_data:
        if (row["id"]==id):
            name=row["name"]
            break
    return{"id":id,"name":name}
    
        




     