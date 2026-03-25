import logging
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from operations import add, subtract, multiply, divide

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    filename="app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    logger.info("Home page accessed")
    return templates.TemplateResponse(
        request,
        "index.html",
        {"result": None, "error": None}
    )


@app.post("/calculate", response_class=HTMLResponse)
def calculate(request: Request, a: float = Form(...), b: float = Form(...), operation: str = Form(...)):
    logger.info("Calculation request received: a=%s, b=%s, operation=%s", a, b, operation)

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            logger.error("Invalid operation requested: %s", operation)
            return templates.TemplateResponse(
                request,
                "index.html",
                {"result": None, "error": "Invalid operation"}
            )

        return templates.TemplateResponse(
            request,
            "index.html",
            {"result": result, "error": None}
        )

    except ValueError as e:
        logger.error("Calculation error: %s", str(e))
        return templates.TemplateResponse(
            request,
            "index.html",
            {"result": None, "error": str(e)}
        )
