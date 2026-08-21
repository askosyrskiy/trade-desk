from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from trade_desk.strategies.spx_iron_fly import SpxIronFly

ROOT = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(ROOT / "templates"))

app = FastAPI(title="trade-desk", version="0.1.0")
app.mount("/static", StaticFiles(directory=str(ROOT / "static")), name="static")


def _iron_fly_context() -> dict:
    strategy = SpxIronFly()
    model = strategy.view_model()
    model["mode"] = strategy.mode.value
    model["broker"] = "tradier (not wired)"
    return {"model": model}


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse("/iron-fly")


@app.get("/iron-fly", response_class=HTMLResponse)
def iron_fly(request: Request) -> HTMLResponse:
    ctx = {"request": request, **_iron_fly_context()}
    return templates.TemplateResponse("iron_fly.html", ctx)


def main() -> None:
    import uvicorn

    uvicorn.run("trade_desk.web.app:app", host="127.0.0.1", port=8000, reload=True)
