"""Main Entrypoint for the script."""
import os
import httpx
import json
from loguru import logger
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketDisconnect

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()
# Define OpenAI client and router
API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID") 
thread_id = None

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
        "OpenAI-Beta": "assistants=v2"
}

async def create_thread() -> str:
    """Create a new thread."""
    url = "https://api.openai.com/v1/threads"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()["id"]


async def send_message(thread_id: str, content: str) -> None:
    """Send a message to the assistant."""
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages"
    async with httpx.AsyncClient() as client:
        payload = {
            "role": "user",
            "content": content
        }
        response = await client.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()

async def stream_response(websocket: WebSocket, thread_id: str) -> None:
    """Stream the assistant's response to the WebSocket."""
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs"
    payload = {
        "assistant_id": ASSISTANT_ID,
        "stream": True
    }
    
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", url, headers=HEADERS, json=payload) as response:
            async for line in response.aiter_lines():
                logger.debug(f"Received line: {line}")
                data = line.strip()
                
                if data.startswith("data: "):
                    try:
                        json_data = json.loads(data[6:])
                        if "delta" in json_data and "content" in json_data["delta"]:
                            for chunk in json_data["delta"]["content"]:
                                if chunk["type"] == "text":
                                    await websocket.send_text(chunk["text"]["value"])
                                    logger.debug(f"Sent text chunk to client: {chunk['text']['value']}")
                    except json.JSONDecodeError:
                        logger.exception("Received non-JSON data, skipping:", data)
                    except KeyError as e:
                        logger.exception(f"Unexpected JSON structure: {e}, data: {json_data}")
                elif data.startswith("event: thread.run.completed"):
                    logger.info("Completed response from assistant.")
                    break



@router.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket) -> None:
    """Handle WebSocket connections for chat."""
    await websocket.accept()
    try:
        # Create a new thread specifically for this WebSocket connection
        thread_id = await create_thread()
        logger.debug(f"Created thread {thread_id} for new WebSocket connection.")

        # Listen for incoming messages from the client
        while True:
            user_message = await websocket.receive_text()
            await send_message(thread_id, user_message)
            await stream_response(websocket, thread_id)

    except WebSocketDisconnect:
        logger.info("WebSocket connection closed.")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        await websocket.send_text(f"Error: {e}")


# Mount static files and add router
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to the Dungeon Master Assistant Chatbot!"}

