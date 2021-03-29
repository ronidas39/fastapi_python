from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def show():
    return {"NAME":"RONI DAS","COUNTRY":"INDIA","company":"abc"}

@app.get("/about")
def show_about():
    return {"ABOUT":"TEST PAGE FOR ABOUT"}