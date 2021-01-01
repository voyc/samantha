#!/usr/bin/env python

# WS server that sends messages at random intervals
# this template demonstrates asyncio and websockets

import asyncio
import websockets
import datetime
import random

# define the coroutine (thread target fn)
async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

# create server object,  wrapping the cooroutine
server = websockets.serve(time, "127.0.0.1", 5678)

# start the thread, wrapping the server object
event_loop = asyncio.get_event_loop()  # get the scheduler
event_loop.run_until_complete(server)
event_loop.run_forever()

