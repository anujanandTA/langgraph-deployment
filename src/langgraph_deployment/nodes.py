from langchain_openai import ChatOpenAI

from .state import State
from .tools import available_tools
from .config import LLM_MODEL, LLM_API_ENDPOINT, LLM_API_KEY

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
