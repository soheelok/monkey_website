import asyncio
import websockets
from serial import Serial
from pyubx2 import UBXReader

async def send_coordinates(websocket, path):
    input_stream = Serial('COM20', 115200)
    ubr_input = UBXReader(input_stream)

    try:
        while True:
            raw_data, parsed_data = ubr_input.read()
            print(parsed_data)

            if parsed_data and parsed_data.identity == 'NAV-HPPOSLLH':
                lat = parsed_data.lat  # Convert to degrees
                lon = parsed_data.lon  # Convert to degrees
                print(f"Latitude: {lat}, Longitude: {lon}")

                message = f"{lat},{lon}"
                print(f"Sent: {message}")

                # Send the coordinates over the WebSocket connection
                await websocket.send(message)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        input_stream.close()

start_server = websockets.serve(send_coordinates, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
