import functools
import time


def read_data(path: str) -> dict[str, list[str]]:
    with open(path, "r") as file:
        return {
            line.split(":")[0]: line.split(":")[1].split()
            for line in file.read().strip().split("\n")
        }


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def count_paths(
    graph: dict[str, list[str]],
    current: str,
    target: str,
) -> int:
    if current == target:
        return 1
    if current not in graph:
        return 0
    # recursively count
    total = 0
    for next in graph[current]:
        total += count_paths(graph, next, target)
    return total


def solve_part_1(graph: dict[str, list[str]]) -> int:
    # part 1 closure for cached path counter
    @functools.cache
    def count_paths(current: str) -> int:
        if current == "out":
            return 1
        if current not in graph:
            return 0
        # recursively count
        return sum(count_paths(next) for next in graph[current])

    return count_paths("you")


def solve_part_2(graph: dict[str, list[str]]) -> int:
    # memoized recursive function to count paths
    @functools.cache
    def count_paths(
        current: str, visited_dac: bool = False, visited_fft: bool = False
    ) -> int:
        if current == "dac":
            visited_dac = True
        if current == "fft":
            visited_fft = True
        allowed_to_exit = visited_dac and visited_fft
        if current == "out" and allowed_to_exit:
            return 1
        if current not in graph:
            return 0
        # recursively count
        total = 0
        for next in graph[current]:
            total += count_paths(next, visited_dac, visited_fft)
        return total

    return count_paths("svr")


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
