from langgraph_deployment.agent import get_agent

if __name__ == "__main__":
    agent = get_agent()
    prompt = "What is your name?"
    resp = agent.invoke(input={"messages": [{"role": "user", "content": prompt}]})
    print(resp)
