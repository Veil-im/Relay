import websockets
from fastapi import FastAPI

app = FastAPI()

@app.websocket("/ping")
async def websocket_endpoint(websocket: websockets.ClientConnection):
    await websocket.accept()
    while True:
        data = await websocket.recv()
        if type(data) == str:
            if data.lower() == "ping":
                await websocket.send("Pong")
            else:
                await websocket.send("Still pong")
        else:
            await websocket.send("Still pong")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)