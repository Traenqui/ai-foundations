from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from fastapi import APIRouter, WebSocket

router = APIRouter()
client = OpenAI()

ASSISTANT_ID = "asst_NITBEVrzyF7i4oDOiHgt2An7"
thread_id = None


class StreamEventhandler(AssistantEventHandler):
    def __init__(self, websocket: WebSocket) -> None:
        self.websocket = websocket

    @override
    def on_text_created(self, text) -> None:
        print("\nassistant > ", end="", flush=True)

    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)
      
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)
  
    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
          if delta.code_interpreter.input:
            print(delta.code_interpreter.input, end="", flush=True)
          if delta.code_interpreter.outputs:
            print("\n\noutput >", flush=True)
            for output in delta.code_interpreter.outputs:
              if output.type == "logs":
                print(f"\n{output.logs}", flush=True)

@router.websocket_route("/ws/chat")
async def chat_websocket(websocket: WebSocket) -> None:
    """Handle WebSocket connections for chat.

    Args:
        websocket (WebSocket): The WebSocket connection object.
    """
    await websocket.accept()
    try:
        if thread_id is None:
            thread = client.beta.threads.create()
            thread_id = thread['id']

        user_message = await websocket.receive_text()
        
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_message)
            
        with client.beta.threads.runs.stream(
            thread_id=thread_id,
            assistant_id=ASSISTANT_ID
        ) as stream:
            stream.until_done()

    except Exception as e:
        print(e)
