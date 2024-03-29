from dotenv import load_dotenv
from langchain.agents.openai_assistant import OpenAIAssistantRunnable

load_dotenv()

interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="openai assistant",
    instructions="You are an expert Python engineer.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-0125-preview",
)


def execute_openai_assistant(request):
    output = interpreter_assistant.invoke({"content": request})
    return output
