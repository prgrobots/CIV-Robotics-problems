import pytest
from unittest.mock import patch
from indoor import process_input, output

# Test cases for the happy path with various realistic test values
@pytest.mark.parametrize("test_input, expected", [
    ("TEST", "test", "happy_path_lowercase"),
    ("MiXeDcAsE", "mixedcase", "happy_path_mixed_case"),
    ("123", "123", "happy_path_numbers"),
    ("test123", "test123", "happy_path_alphanumeric"),
    ("", "", "happy_path_empty_string")
])
def test_process_input_happy_path(test_input, expected, test_id):
    # Act
    with patch('builtins.input', return_value=test_input):
        process_input = input("Enter a string: ")
        result = process_input.lower()

    # Assert
    assert result == expected, f"Test failed for {test_id}"

# Test cases for edge cases
@pytest.mark.parametrize("test_input, expected", [
    ("    ", "    ", "edge_case_spaces"),
    ("\t\n", "\t\n", "edge_case_whitespace_chars"),
    ("!@#$%^&*()_+", "!@#$%^&*()_+", "edge_case_special_chars"),
    ("长城", "长城", "edge_case_unicode_chars"),
    ("🙂😉", "🙂😉", "edge_case_emojis")
])
def test_process_input_edge_cases(test_input, expected, test_id):
    # Act
    with patch('builtins.input', return_value=test_input):
        process_input = input("Enter a string: ")
        result = process_input.lower()

    # Assert
    assert result == expected, f"Test failed for {test_id}"

# Test cases for error cases are not applicable here since input() will always return a string
# and the .lower() method can be called on any string without causing an error.
# However, if we were to consider the environment where input() might be interrupted or
# receive EOF, we could mock this behavior as follows:

@pytest.mark.parametrize("side_effect, test_id", [
    (EOFError, "error_case_eof"),
    (KeyboardInterrupt, "error_case_interrupt")
])
def test_process_input_error_cases(side_effect, test_id):
    # Act
    with patch('builtins.input', side_effect=side_effect):
        with pytest.raises(side_effect):
            process_input = input("Enter a string: ")

    # Assert
    # The assert is implicit in the pytest.raises context manager, which checks that the expected exception is raised.
