import concurrent.futures
import asyncio
import websockets
import queue

addr = 'ws://localhost:50001'
socket = None
q = queue.SimpleQueue()

async def openSocket(uri):
	global socket
	socket = await websockets.connect(uri)

async def closeSocket():
	await socket.close()
	await asyncio.sleep(.1)  # give sendLoop time to exit

def keyboardLoop():
	while True:
		s = input()  # blocking this executor thread
		if s == 'q':
			break;
		q.put(s)

async def waitForKeyboard(loop, executor):
	await asyncio.wait(
		fs={
			loop.run_in_executor(executor, keyboardLoop)
		},
		return_when=asyncio.ALL_COMPLETED
	)

async def sendLoop():
	while socket.state == 1: # State.OPEN:
		try:
			s = q.get(block=False)
		except queue.Empty:
			await asyncio.sleep(.08)  # like yield
		else:	
			await socket.send(s)

async def receiveLoop():
	while True:
		try:
			s = await socket.recv()
		except websockets.exceptions.ConnectionClosed:
			break
		else:
			print(s)

loop = asyncio.get_event_loop()
loop.run_until_complete( openSocket( addr))
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
loop.create_task( sendLoop())   # create_task replaces ensure_future as of python 3.7
loop.create_task( receiveLoop())
loop.run_until_complete( waitForKeyboard(loop,executor))
loop.run_until_complete( closeSocket())
loop.close()
