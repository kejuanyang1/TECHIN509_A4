"""
Description 
TECHIN 509
Week 4: Lab Submission (GitHub Version Control) 
Created by: Kejuan Yang
Date: 2023/10/22
"""

"""
Flood Fill Function
Flood-fill is a common algorithm used to fill connected regions of the board with a new value based on a specified condition. The code takes an input board, an old value, a new value, and coordinates (x, y) as arguments. It recursively updates the board by changing the old value to the new value for all connected cells.
"""

def flood_fill(input_board, old, new, x, y):
    """
    Returns a board with old values replaced with new values through flood-filling, starting from coordinates x, y.

    Args:
        input_board (List[str]): The input board.
        old (str): Value to be replaced.
        new (str): Value that replaces the old.
        x (int): X-coordinate of the flood start point.
        y (int): Y-coordinate of the flood start point.

    Returns:
        List[str]: Modified board.
    """
    # Ensure input_board is a list of strings and all rows have the same length
    assert isinstance(input_board, list), "Input board should be a list of strings."
    assert all(isinstance(row, str) and len(row) == len(input_board[0]) for row in input_board), "All rows should have the same length."
    
    width, length = len(input_board), len(input_board[0])
    
    # Ensure x and y are within bounds
    assert 0 <= x < width and 0 <= y < length, "(x, y) coordinates are out of bounds."

    # In case change of input
    input_board = input_board.copy()
    
    if input_board[x][y] != old:
        raise ValueError(f"Start value at ({x}, {y}) is {input_board[x][y]}, not {old}!")
    
    # Modify the value
    s_list = list(input_board[x])
    s_list[y] = new
    input_board[x] = ''.join(s_list)
    
    # Recursive function
    if x > 0 and input_board[x - 1][y] == old:
        input_board = flood_fill(input_board, old, new, x - 1, y)
    if x < width - 1 and input_board[x + 1][y] == old:
        input_board = flood_fill(input_board, old, new, x + 1, y)
    if y > 0 and input_board[x][y - 1] == old:
        input_board = flood_fill(input_board, old, new, x, y - 1)
    if y < length - 1 and input_board[x][y + 1] == old:
        input_board = flood_fill(input_board, old, new, x, y + 1)
    
    return input_board

# Default test board
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

# Additional test board
additional_board = [
    "####.................",
    "#....................",
    "##...................",
    "###..................",
    "####.................",
    "#####################",
    ".....................",
]

# Testing the flood_fill function on the default board
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
print('\n')

# Expected output for the default board:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....


# Testing the flood_fill function on the additional board
modified_additional_board = flood_fill(input_board=additional_board, old=".", new="*", x=3, y=4)

for row in modified_additional_board:
    print(row)

# Expected output for the additional board:
# ####*****************
# #********************
# ##*******************
# ###******************
# ####*****************
# #####################
# .....................

