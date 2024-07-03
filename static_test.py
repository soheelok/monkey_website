import asyncio
import websockets

async def send_static_coordinates(websocket, path):
    try:
        while True:
            lat = 3.012711  # Static latitude
            lon = 101.741318  # Static longitude
            message = f"{lat},{lon}"
            print(f"Sent: {message}")

            # Send the static coordinates over the WebSocket connection
            await websocket.send(message)
            await asyncio.sleep(1)  # Send updates every second

    except Exception as e:
        print(f"Error: {e}")

start_server = websockets.serve(send_static_coordinates, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
