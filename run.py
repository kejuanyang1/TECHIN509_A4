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


def flood_fill(input_board, old, new, x, y):
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str]): The input board
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    input_board = input_board.copy()
    # In case change of input
    width, length = len(input_board), len(input_board[0])
    # Exception
    if input_board[x][y] != old:
        raise AttributeError(f'Start value at (x, y) is {input_board[x][y]}, not {old}!')
    # Modify the value
    s_list = list(input_board[x])
    s_list[y] = new
    input_board[x] = ''.join(s_list)
    # Recursive function
    if x > 0 and input_board[x-1][y] == old:
        input_board = flood_fill(input_board, old, new, x-1, y)
    if x < width - 1 and input_board[x+1][y] == old:
        input_board = flood_fill(input_board, old, new, x+1, y)
    if y > 0 and input_board[x][y-1] == old:
        input_board = flood_fill(input_board, old, new, x, y-1)
    if y < length - 1 and input_board[x][y+1] == old:
        input_board = flood_fill(input_board, old, new, x, y+1)
    return input_board


# Unit Test 1
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
print('\n\n')

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

# Unit Test 2
modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)

# Expected output:
#~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~##########~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#####~~
#~~~~###............#~~
#~~~~#............###~~
#~~~~##############~~~~