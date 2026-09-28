from fastapi import FastAPI
from routers.student_router import StudentRouter

app = FastAPI()

app.include_router(StudentRouter)


@app.get("/")
def home():
    return {"message": "Student API is running! Go to /docs for Swagger UI"}

# Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force