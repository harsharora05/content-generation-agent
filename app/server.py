from fastapi import FastAPI, HTTPException,Body
from fastapi.responses import JSONResponse
from model.api_response_model import ApiResponse
from pipeline import run_pipeline
import logging



app = FastAPI()
logger = logging.getLogger("contentagent")


@app.post("/generate",response_model=ApiResponse)
async def generate(query:str=Body(...,embed=True)):
    try:
        if query is None or not str(query).strip():
            raise JSONResponse(
                status_code=400,
                content={
                    "response" : "Query is required"
                }
            )

        response = await run_pipeline(query)
        return JSONResponse(
            status_code=200,
            content={
            "response" : response}
            )
    except HTTPException :
        raise
    except Exception:
        logger.exception("unhandled error")
        raise JSONResponse(
            status_code= 500,
            content={
            "response" : "Internal server error please try again later"}
            )
