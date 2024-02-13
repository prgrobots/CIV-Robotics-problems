# camel.py

def camel_to_snake(camel_case):
    """
    Convert a variable name from camel case to snake case.

    Args:
        camel_case (str): The variable name in camel case.

    Returns:
        str: The variable name in snake case.
    """
    # TODO: Implement the conversion logic
    pass

if __name__ == "__main__":
    user_input = input("Enter a variable name in camel case: ")
    snake_case_output = camel_to_snake(user_input)
    print("Snake case:", snake_case_output)
