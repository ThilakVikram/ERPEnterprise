from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Thilak Vikram R is Software Developer\n working in Software Company"}