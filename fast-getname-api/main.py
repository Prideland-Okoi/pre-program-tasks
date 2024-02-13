#!/usr/bin/python3
# Author - prideland.okoi@gmail.com
# API DOC - https://get-name-api.onrender.com/docs
import uvicorn
from fastapi import FastAPI
from routers import get_fullname, get_pdf


app = FastAPI()


app.include_router(get_fullname.router)
app.include_router(get_pdf.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
