# extensions.py

def determine_media_type(file_name):
    """
    Determine the media type based on the file's extension.

    Args:
        file_name (str): The name of the file.

    Returns:
        str: The media type of the file.
    """
    # TO DO: Implement the logic for determining the media type
    pass

if __name__ == "__main__":
    user_file_name = input("Enter the name of the file: ")
    media_type = determine_media_type(user_file_name)
    print(f"The media type of the file is {media_type}.")
