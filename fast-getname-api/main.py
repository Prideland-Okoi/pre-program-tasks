#!/usr/bin/python3
# Author - prideland.okoi@gmail.com
# API DOC - https://get-name-api.onrender.com/docs
from fastapi import FastAPI
from routers.get_fullname import router as get_namerouter

app = FastAPI()

app.include_router(get_namerouter)
