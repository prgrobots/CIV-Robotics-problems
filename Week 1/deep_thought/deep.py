# deep.py

def answer_to_life_universe_everything(user_input):
    """
    Determine if the provided user input is the answer to the Great Question of Life, the Universe, and Everything.

    Args:
        user_input (str): The user's input.

    Returns:
        str: "Yes" if the input is 42, "forty-two", or "forty two" (case-insensitive), otherwise "No".
    """
    # TO DO: Implement the logic for determining the answer
    user_input = user_input.lower()
    if  any(word in user_input for word in ('42','forty-two','forty two')):
        result = "Yes"
        return result
    else: return 'No'


if __name__ == "__main__":
    user_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    result = answer_to_life_universe_everything(user_answer)
    print(result)
