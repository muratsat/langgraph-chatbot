    # answer = graph.invoke({"messages": [("user", "Hello")]}, { "configurable": { "thread_id": thread_id }})
    # # print(answer)

    # if "final_response" in answer:
    #     print(answer["final_response"])
from dotenv import load_dotenv
load_dotenv(override=True)

from graph import graph



if __name__ == "__main__":
    thread_id = "42"
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        answer = graph.invoke({"messages": [("user", user_input)]}, { "configurable": { "thread_id": thread_id }})
        print(answer["final_response"])
