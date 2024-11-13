from dotenv import load_dotenv
load_dotenv()

from graph import graph


def stream_graph_updates(user_input: str, thread_id: str = "1"):
    for event in graph.stream({"messages": [("user", user_input)]}, { "configurable": { "thread_id": thread_id }}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break
