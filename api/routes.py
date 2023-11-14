from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles

from repositories import RequestsRepository
from schemas import InputRequestSchema, RequestSchema
from services.requests_service import RequestsService

app = FastAPI()
request_service = RequestsService(RequestsRepository())

app.mount("/static", StaticFiles(directory="./build/static"), name="static")


@app.get("/api/ping")
async def ping():
    return JSONResponse(status_code=200, content={"msg": "OK"})


@app.get("/api/query")
async def query(request: InputRequestSchema = Depends()):
    response = await request_service.accept_request(request)
    return JSONResponse(status_code=200, content={"msg": response})


@app.get("/api/history")
async def history():
    serialized = [item.model_dump() for item in await request_service.get_requests_history()]
    return JSONResponse(status_code=200, content={"history": serialized})


@app.get("/admin-panel")
async def admin_panel():
    return FileResponse("./build/index.html")
