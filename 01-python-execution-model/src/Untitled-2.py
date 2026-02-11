"""
Day 1: Python Execution Model & Mutability

This script demonstrates:
- Name binding vs copying
- Mutable vs immutable objects
- Why shared mutable state is dangerous
- How to safely update state using copies
"""

def add_message_safely(memory, message):
    """
    Returns a new list with the message added.
    Does NOT mutate the original list.
    """
    new_memory = memory.copy()
    new_memory.append(message)
    return new_memory


def main():
    # Immutable example
    x = 10
    y = x
    x = 20

    print("Immutable example:")
    print("x:", x)
    print("y:", y)
    print()

    # Mutable example (safe pattern)
    agent_memory = []
    tool_memory = agent_memory.copy()

    agent_memory = add_message_safely(agent_memory, "User asked a question")
    tool_memory = add_message_safely(tool_memory, "Tool added metadata")

    print("Mutable example with safe copying:")
    print("Agent memory:", agent_memory)
    print("Tool memory:", tool_memory)


if __name__ == "__main__":
    main()
