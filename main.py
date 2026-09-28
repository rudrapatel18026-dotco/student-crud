from fastapi import FastAPI
from routers.student_router import StudentRouter

app = FastAPI()

app.include_router(StudentRouter)


from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette import status

app = FastAPI()

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")

# Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force