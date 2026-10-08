from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Tell FastAPI where our HTML files are located
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html"
)


# API endpoint
@app.get("/api/hello")
async def hello(name: str = "Developer"):
    return {
        "message": f"Hello, {name}! 👋",
        "status": "success"
    }