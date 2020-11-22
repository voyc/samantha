#!/usr/bin/env python3
# synctemplate.py

import asyncio
import time

async def coroutine():
	while True:
		print("One")
		await asyncio.sleep(1)
		print("two")

async def wrapper():
	await asyncio.gather(coroutine())

asyncio.run(wrapper())
