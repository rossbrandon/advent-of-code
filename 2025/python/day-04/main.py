import time


def read_data(path: str) -> list[list[str]]:
    with open(path, "r") as file:
        return [list(row) for row in file.read().strip().split("\n")]


def remove_rolls(grid: list[list[str]], mutate: bool = False) -> int:
    """
    Removes rolls of paper from the grid that are accessible by a forklift.
    Returns the number of rolls removed.
    """
    rolls_removed = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != "@":
                continue
            # get the row before and after the current row
            adjacent_rows = grid[max(0, r - 1) : r + 2]
            # get the column before and after the current column for each adjacent row
            # this is the area to check
            adjacent_area = [
                adjacent_cols[max(0, c - 1) : c + 2] for adjacent_cols in adjacent_rows
            ]
            adjacent_roll_count = sum(row.count("@") for row in adjacent_area)
            # if the adjacent roll count is less than or equal to 4, then the current roll can be accessed by a forklift
            # less than or equal because we need to count the current roll as well
            if adjacent_roll_count <= 4:
                rolls_removed += 1
                if mutate:
                    grid[r][c] = "x"
    return rolls_removed


def solve_part_1(grid: list[list[str]]) -> int:
    return remove_rolls(grid)


def solve_part_2(grid: list[list[str]]) -> int:
    rolls_removed = 0
    # copy the current grid so we can modify and track removal state over iterations
    grid_copy = [row[:] for row in grid]
    while True:
        rolls_removed_this_iteration = remove_rolls(grid_copy, mutate=True)
        if rolls_removed_this_iteration == 0:
            break
        rolls_removed += rolls_removed_this_iteration
    return rolls_removed


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def main():
    data = read_data("data.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(data)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")

    # Part 2
    start_time = time.perf_counter()
    part_2 = solve_part_2(data)
    end_time = time.perf_counter()
    print(f"Part 2: {part_2} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
