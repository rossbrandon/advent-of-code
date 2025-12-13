import time
from itertools import combinations

from shapely.geometry import Polygon, box


def read_data(path: str) -> list[list[int]]:
    with open(path, "r") as file:
        data = file.read().strip().split("\n")
        return [list(map(int, line.split(","))) for line in data]


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(data: list[list[int]]) -> int:
    max_area = 0
    for a, b in combinations(data, 2):
        area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
        if area > max_area:
            max_area = area
    return max_area


def solve_part_2(data: list[list[int]]) -> int:
    # create a polygon from the coordinates
    polygon = Polygon([(x, y) for x, y in data])

    # define a function to be used as a key for sorting
    def get_area(pair: tuple[tuple[int, int], tuple[int, int]]) -> int:
        a, b = pair
        return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

    pairs = sorted(combinations(data, 2), key=get_area, reverse=True)
    for a, b in pairs:
        x1, y1 = min(a[0], b[0]), min(a[1], b[1])
        x2, y2 = max(a[0], b[0]), max(a[1], b[1])
        rect = box(x1, y1, x2, y2)

        if polygon.contains(rect):
            return get_area((a, b))

    return 0


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
