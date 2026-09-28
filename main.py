from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.student_router import StudentRouter

app = FastAPI(title="Student Management API")

# Register the student routes
app.include_router(StudentRouter)


@app.get("/")
def home():
    return RedirectResponse(url="/docs")

# Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force