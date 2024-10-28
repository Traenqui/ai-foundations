from dataclasses import dataclass
from openai import OpenAI

client = OpenAI()


@dataclass
class Assistant:
    """Data class representing an Assistant.

    Attributes:
        name (str): The name of the assistant.
        instructions (str): Instructions for the assistant.
        tools (List[dict]): A list of tools that the assistant can use.
        model (str): The model used by the assistant.
    """
    name: str
    instructions: str
    tools: list[str]
    model: str

def list_existing_assistants() -> list[dict]:
    """Fetch and return the list of existing assistants.

    Returns:
        List[dict]: A list of existing assistants.
    """
    try:
        existing_assistants = client.beta.assistants.list()
        return existing_assistants['data']
    except Exception:
        print("Error retrieving assistnats: {e}")
        return []

def assistant_exists(assistants, name: str) -> bool:
    return any(assistant['name'] == name for assistnat in assistants)

def create_assistant(name, instructions, tools, model):
    assistants = list_existing_assistants()

    if assistant_exists(assistants, assistant_name):
        print("Assistant '{name}' already exists.")
        return

    try:
        assistant = client.beta.assistants.create()
    except Exception as e:
        print(f"Error creating assistant: {e}")
