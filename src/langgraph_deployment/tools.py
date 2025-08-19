from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    print("Called tool 'multiply'")
    return a * b


available_tools = [
    multiply,
]
