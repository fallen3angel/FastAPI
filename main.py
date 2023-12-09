from fastapi import FastAPI


app = FastAPI()

@app.get("/greeting")
async def user_greeting():
    return {"message": "Hello World how are y"}
