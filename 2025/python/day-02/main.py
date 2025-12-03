def read_data(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().strip().split(",")


def is_invalid_id(id: int) -> bool:
    id_str = str(id)
    midpoint = len(id_str) // 2
    first_half, second_half = id_str[:midpoint], id_str[midpoint:]
    return first_half == second_half


def solve_part_1_brute_force(data: list[str]) -> int:
    invalid_ids = []
    for id_range in data:
        start, end = id_range.split("-")
        for id in range(int(start), int(end) + 1):
            if is_invalid_id(id):
                invalid_ids.append(id)
    return sum(invalid_ids)


def get_pattern_lengths(id_len: int, is_flexible_pattern: bool = False) -> list[int]:
    # Part 1 only allows even pattern lengths, Part 2 allows all possible pattern lengths
    if is_flexible_pattern:
        # Get all possible pattern lengths that divide evenly and can repeat at least twice
        return [i for i in range(1, id_len // 2 + 1) if id_len % i == 0]
    else:
        # Get only the even pattern length if it exists
        return [id_len // 2] if id_len % 2 == 0 else []


def get_invalid_ids(data: list[str], is_flexible_pattern: bool = False) -> set[int]:
    """Get all invalid IDs in the given data for both Part 1 and Part 2."""
    invalid_ids: set[int] = set()
    for id_range in data:
        min_id, max_id = map(int, id_range.split("-"))
        min_len = len(str(min_id))
        max_len = len(str(max_id))
        id_len_range = range(min_len, max_len + 1)
        # check all possible pattern lengths for each id length
        for id_len in id_len_range:
            pattern_lengths = get_pattern_lengths(id_len, is_flexible_pattern)
            # check all possible patterns for each pattern length
            for pattern_length in pattern_lengths:
                start_pattern = 10 ** (pattern_length - 1)
                end_pattern = 10**pattern_length
                repetitions = id_len // pattern_length
                # check all possible repetitions for each pattern
                for pattern in range(start_pattern, end_pattern):
                    potential_id = int(str(pattern) * repetitions)
                    if min_id <= potential_id <= max_id:
                        invalid_ids.add(potential_id)
    return invalid_ids


def solve_part_1(data: list[str]) -> int:
    return sum(get_invalid_ids(data, is_flexible_pattern=False))


def solve_part_2(data: list[str]) -> int:
    return sum(get_invalid_ids(data, is_flexible_pattern=True))


def main():
    data = read_data("data.txt")
    print("Part 1: ", solve_part_1(data))
    print("Part 2: ", solve_part_2(data))


if __name__ == "__main__":
    main()
