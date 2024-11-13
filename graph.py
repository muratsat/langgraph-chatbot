from typing import Literal
from langgraph.graph import START, END, MessagesState, StateGraph
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from tools import search_tool, web_search_tool

tools = [search_tool, web_search_tool]
model = ChatOpenAI(model="gpt-4o").bind_tools(tools)
tools_node = ToolNode(tools=tools)


def llm_node(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    return { "messages": [response] }


def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    # If the LLM makes a tool call, then we route to the "tools" node
    if last_message.tool_calls:
        return "tools"
    # Otherwise, we stop (reply to the user)
    return END


graph_builder = StateGraph(MessagesState)

graph_builder.add_node("llm", llm_node)
graph_builder.add_node("tools", tools_node)

graph_builder.add_edge(START, "llm")
graph_builder.add_conditional_edges("llm", should_continue)
graph_builder.add_edge("tools", "llm")


memory = MemorySaver()

graph = graph_builder.compile(checkpointer=memory)
