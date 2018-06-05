#WORK IN PROGRESS, INSPIRED BY RAJ WORK

import asyncio
import websockets
import sys



async def get_processed_image(websocket, path):
    while True:
        await websocket.recv()

        await websocket.send(str(match))

def main():
    # start websockets server
    print("Starting server...")
    start_server = websockets.serve(get_processed_image, '0.0.0.0', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    sys.exit(main())