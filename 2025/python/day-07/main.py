import time
from collections import Counter

STARTING_POINT = "S"
SPLITTER = "^"


def read_data(path: str) -> list[list[str]]:
    with open(path, "r") as file:
        return [list(line) for line in file.read().strip().split("\n")]


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(data: list[list[str]]) -> int:
    count = 0
    beams = {data[0].index(STARTING_POINT)}
    for line in data:
        next_beams = set()
        for col in beams:
            if line[col] == SPLITTER:
                count += 1
                next_beams.update({col - 1, col + 1})
            else:
                next_beams.add(col)
        beams = next_beams
    return count


def solve_part_2(data: list[list[str]]) -> int:
    start_index = data[0].index(STARTING_POINT)
    timelines = {start_index: 1}
    for line in data:
        count = Counter()
        for col, timeline_count in timelines.items():
            if line[col] == SPLITTER:
                count[col - 1] += timeline_count
                count[col + 1] += timeline_count
            else:
                count[col] += timeline_count
        timelines = count
    return sum(timelines.values())


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
