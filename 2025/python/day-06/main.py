import math
import time


def read_data(path: str) -> tuple[list[tuple[int, ...]], list[str]]:
    """Read the data from the file and return the numbers and operators as separate lists."""
    with open(path, "r") as file:
        data = file.read().split("\n")
        lines = data[:-1]
        operators = data[-1].split()
        return lines, operators


def transpose(lines: list[str]) -> list[tuple[int, ...]]:
    return zip(*lines)


def parse_part_1(lines: list[str]) -> list[tuple[int, ...]]:
    """Parse numbers by splitting each row, then transpose to get problem columns."""
    numbers = [tuple(map(int, row.split())) for row in lines]
    return transpose(numbers)


def parse_part_2(lines: list[str]) -> list[tuple[str, ...]]:
    """Parse characters in each column: spaces and numbers, then transpose to get problem columns."""
    return list(transpose(lines))


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(raw_numbers: list[tuple[int, ...]], operators: list[str]) -> int:
    numbers = parse_part_1(raw_numbers)
    total = 0
    for i, num in enumerate(numbers):
        if operators[i] == "+":
            total += sum([n for n in num])
        else:
            total += math.prod([n for n in num])
    return total


def is_separator(col: tuple[str, ...]) -> bool:
    """Check if a given tuple is all spaces indicating it is a true separator."""
    return all(c == " " for c in col)


def col_to_num(col: tuple[str, ...]) -> int:
    return int("".join(c for c in col if c != " "))


def get_number_groups(columns: list[tuple[int, ...]]) -> list[list[int]]:
    groups = []
    current = []
    for col in columns:
        if is_separator(col):
            groups.append(current)
            current = []
            continue
        current.append(col)
    if current:
        groups.append(current)
    return [[col_to_num(col) for col in group] for group in groups]


def solve_part_2(raw_numbers: list[tuple[int, ...]], operators: list[str]) -> int:
    numbers = parse_part_2(raw_numbers)
    total = 0
    # Get the groups of numbers
    groups = get_number_groups(numbers)
    for i, group in enumerate(groups):
        # Get the final numbers from the group
        if operators[i] == "+":
            total += sum([n for n in reversed(group)])
        else:
            total += math.prod([n for n in reversed(group)])
    return total


def main():
    numbers, operators = read_data("data.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(numbers, operators)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")

    # Part 2
    start_time = time.perf_counter()
    part_2 = solve_part_2(numbers, operators)
    end_time = time.perf_counter()
    print(f"Part 2: {part_2} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
