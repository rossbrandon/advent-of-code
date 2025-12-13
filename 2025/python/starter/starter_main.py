import time


def read_data(path: str) -> list[list[int]]:
    with open(path, "r") as file:
        return [map(int, line.split()) for line in file.read().strip().split("\n")]


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(data: list[list[int]]) -> int:
    return 0


def main():
    data = read_data("test.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(data)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
