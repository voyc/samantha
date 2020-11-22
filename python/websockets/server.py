''' server.py   testing websockets server  '''

import asyncio
import websockets

async def echo(websocket, path):
	async for message in websocket:
		response = f'echo: {message}'
		print(response)
		await websocket.send(response)

loop = asyncio.get_event_loop()
loop.run_until_complete( websockets.serve(echo, 'localhost', 8765))
loop.run_forever()

