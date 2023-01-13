#simple websockets brocaster
import asyncio
import websockets
clients = [] #to store all connected cleints

#handler for socket message activities
async def handler(websocket, path):
	#print(path) #path is not used currently
	userName='unknown'
	if websocket not in clients:
		clients.append(websocket) #append new cleint to the array
		
	async for message in websocket:
		print(message,'received from client') #print to console
		if message=='getUsers':
			websock.send("USERS," + len(clients))
		else:
			await brocast(message) #send message to all clents

async def brocast(msg):
	print(msg,' brocasting') #print to console

	#iterate the clients
	for websock in clients:
		try:
			await websock.send(msg) #send message to each client
		except websockets.exceptions.ConnectionClosed:
			#remove the client when it disconnects
			print("Client disconnected.  Do cleanup")
			clients.remove(websock)
			
async def brocast(msg):
	print(msg,' brocasting') #print to console

	#iterate the clients
	for websock in clients:
		try:
			await websock.send(msg) #send message to each client
		except websockets.exceptions.ConnectionClosed:
			#remove the client when it disconnects
			print("Client disconnected.  Do cleanup")
			clients.remove(websock)
			#pass

#starts the service and run forever
loop = asyncio.new_event_loop() #get an event loop
asyncio.set_event_loop(loop) #set the event loop to asyncio

loop.run_until_complete(
	websockets.serve(handler, '', 4545) #setup the websocket service and handler
	) #hook to localhost:4545
loop.run_forever() #keep it running
