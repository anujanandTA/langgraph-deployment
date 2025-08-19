from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

LLM_API_KEY = os.environ["LLM_API_KEY"]
LLM_API_ENDPOINT = os.environ["LLM_API_ENDPOINT"]
LLM_MODEL = os.environ["LLM_MODEL"]


class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    print("Called tool 'multiply'")
    return a * b


available_tools = [
    multiply,
]

llm = ChatOpenAI(
    model=LLM_MODEL,
    base_url=LLM_API_ENDPOINT,
    api_key=LLM_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

llm_with_tools = llm.bind_tools(available_tools)


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
tool_node = ToolNode(tools=available_tools)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()

resp = graph.invoke(
    input={"messages": [{"role": "user", "content": "Multiply 2 with 789."}]}
)
print(resp)