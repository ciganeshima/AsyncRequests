import json
import asyncio
from asyncio import sleep
from client import session
from fastapi import FastAPI

app = FastAPI()

CHECK_TIMEOUT = False


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/get_data/1")
async def first_data():
    with open('data_source/first_data.json') as json_file:
        data = json.load(json_file)
    if CHECK_TIMEOUT:
        # check timeout handling
        await sleep(4)
    return data


@app.get("/get_data/2")
async def second_data():
    a = 0
    with open('data_source/second_data.json') as json_file:
        data = json.load(json_file)
    return data


async def req(num):
    try:
        async with session.get(f"http://0.0.0.0:88/get_data/{num}", timeout=2) as response:
            result = await response.json()
        return result
    except asyncio.exceptions.TimeoutError:
        print(f'#Timeout in {num} source of data')
        return None


@app.get("/get_data")
async def get_data():
    first_task = asyncio.create_task(req(1))
    second_task = asyncio.create_task(req(2))
    first_result, second_result = await asyncio.gather(first_task, second_task)
    if not first_result:
        return second_result
    if not second_result:
        return first_result
    else:
        result = first_result + second_result
    sorted_result = sorted(result, key=lambda d: d['id'])
    return sorted_result
