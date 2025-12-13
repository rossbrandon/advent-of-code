import time
from dataclasses import dataclass
from typing import Generator


@dataclass
class TreeRegion:
    width: int
    height: int
    total_boxes: int


def read_data(path: str) -> Generator[TreeRegion, None, None]:
    with open(path, "r") as file:
        for line in file:
            if "x" in line:
                dimensions, boxes = line.split(":")
                w, h = map(int, dimensions.split("x"))
                total_boxes = sum(int(x) for x in boxes.split())
                yield TreeRegion(w, h, total_boxes)


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(data: Generator[TreeRegion, None, None]) -> int:
    count = 0
    for region in data:
        slots = (region.width // 3) * (region.height // 3)
        if slots >= region.total_boxes:
            count += 1
    return count


def main():
    data = read_data("data.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(data)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
