from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the main page."""
    return templates.TemplateResponse(
        request,
        "index.html",
        {"count": 0}
    )

@app.get("/count/{current_count}", response_class=HTMLResponse)
async def increment_counter(request: Request, current_count: int):
    """Increment counter and return updated HTML."""
    new_count = current_count + 1
    return f"""
    <p id="counter" hx-get="/count/{new_count}" hx-trigger="click" hx-swap="outerHTML">
        Count: {new_count}
    </p>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request):
    """Handle form submission."""
    form_data = await request.form()
    name = form_data.get("name", "")
    if not name:
        return '<p id="result" class="error">Please enter your name</p>'
    return f'<p id="result" class="ok">Hello, {name}!</p>'

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
