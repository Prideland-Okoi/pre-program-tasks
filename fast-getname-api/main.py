#!/usr/bin/python3
# Author - prideland.okoi@gmail.com
from fastapi import FastAPI
from routers.get_fullname import router as get_namerouter

app = FastAPI()

app.include_router(get_namerouter)
