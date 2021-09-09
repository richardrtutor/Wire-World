from typing import List
import time
from termcolor import colored


def clear_screen() -> None:
    # Taken from https://stackoverflow.com/a/2084521
    print(chr(27) + "[2J")


def show_cell(cell: int) -> str:
    # TODO
    if cell == 1:
        return colored(" ", on_color="on_red")
    elif cell == 2:
        return colored(" ", on_color="on_blue")
    elif cell == 9:
        return colored(" ", on_color="on_white")
    elif cell == 0:
        return colored(" ", on_color="on_magenta")
    else:
        return " "


def show_grid(grid: List[List[int]]) -> str:
    lines = []
    for row in grid:
        line = []
        for cell in row:
            line.append(show_cell(cell))
        lines.append("".join(line))
    return "\n".join(lines)


def next_grid(grid: List[List[int]]) -> List[List[int]]:
    new_grid = []
    for row_i, row in enumerate(grid):
        new_row = []
        for col_i, cell in enumerate(row):
            new_row.append(next_cell(cell, neighbors(grid, row_i, col_i)))
        new_grid.append(new_row)
    return new_grid


def next_cell(cell: int, neighbors: List[int]) -> int:
    # TODO
    number_live_neighbors = sum(neighbors)
    if cell == 0:
        return 0
    elif cell == 1 and number_live_neighbors >= 9:
        if number_live_neighbors > 23:
            return 1
        else:
            return 9
    elif cell == 9:
        return 2
    elif cell == 1:
        return 1
    elif cell == 2:
        return 1


def neighbors(grid: List[List[int]], row_i: int, col_i: int) -> List[int]:
    result = []
    positions = [
        (row_i - 1, col_i),  # up
        (row_i + 1, col_i),  # down
        (row_i, col_i - 1),  # left
        (row_i, col_i + 1),  # right
        (row_i - 1, col_i - 1),  # up left
        (row_i - 1, col_i + 1),  # up right
        (row_i + 1, col_i - 1),  # down left
        (row_i + 1, col_i + 1),  # down right
    ]
    for r, c in positions:
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            result.append(grid[r][c])
    return result


def main() -> None:
    # TODO: edit this grid to set up the XOR gate from Wireworld's wikipedia page
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 9, 1, 1, 1, 1, 2, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 9, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 9, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(len(grid[0]))
    while True:
        print(show_grid(grid))
        grid = next_grid(grid)
        time.sleep(.2)
        clear_screen()


if __name__ == "__main__":
    main()
