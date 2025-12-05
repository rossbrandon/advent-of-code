import time


def read_data(path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(path, "r") as file:
        parts = file.read().strip().split("\n\n")
        fresh_ingredient_ranges = [
            tuple(map(int, r.split("-"))) for r in parts[0].split("\n")
        ]
        available_ingredient_ids = [int(i) for i in parts[1].split("\n")]
        return fresh_ingredient_ranges, available_ingredient_ids


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def solve_part_1(
    fresh_ingredient_ranges: list[tuple[int, int]], available_ingredient_ids: list[int]
) -> int:
    fresh_ingredient_count = 0
    for i in available_ingredient_ids:
        if any(start <= i <= end for start, end in fresh_ingredient_ranges):
            fresh_ingredient_count += 1
    return fresh_ingredient_count


def solve_part_2(fresh_ingredient_ranges: list[tuple[int, int]]) -> int:
    fresh_id_count = 0
    tracked_range: tuple[int, int] | None = None
    # sort to merge overlapping/adjacent ranges
    for ir in sorted(fresh_ingredient_ranges):
        start, end = ir
        if tracked_range is None:
            tracked_range = (start, end)
        else:
            # extend the tracked range if overlapping
            if start <= tracked_range[1] + 1:
                tracked_range = (tracked_range[0], max(tracked_range[1], end))
            # no overlap - count the tracked range and start a new one
            else:
                fresh_id_count += tracked_range[1] - tracked_range[0] + 1
                tracked_range = (start, end)

    # count the final tracked range
    if tracked_range is not None:
        fresh_id_count += tracked_range[1] - tracked_range[0] + 1

    return fresh_id_count


def main():
    fresh_ingredient_ranges, available_ingredient_ids = read_data("data.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(fresh_ingredient_ranges, available_ingredient_ids)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")

    # Part 2
    start_time = time.perf_counter()
    part_2 = solve_part_2(fresh_ingredient_ranges)
    end_time = time.perf_counter()
    print(f"Part 2: {part_2} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
