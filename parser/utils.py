def get_position_info(content: str, position: int):
    """
    This function is used to retrieve the position details of a character within a given text.
    It returns the line number, column number, and the content of the corresponding line.

    Args:
        content (str): The input text containing multiple lines.
        position (int): The character position in the text. 
                        If negative, it is adjusted to the last character.

    Returns:
        Tuple[int, int, str]: 
            - line (int): The line number where the position is located (starting from 1).
            - column (int): The column number in the corresponding line (starting from 1).
            - line (str): The content of the line containing the character,.
    """
    if position < 0:
        position = len(content) - 1

    line = ''
    lineno = 0
    counter = 0
    for line in content.splitlines():
        lineno += 1
        counter += len(line) + 1  # 1: Include the newline character

        if counter >= position:
            break
    
    index = position - (counter - len(line))

    return lineno, index + 1, line.strip()
