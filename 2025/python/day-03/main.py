def read_data(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().strip().split("\n")


def get_highest_number_in_range(
    digits: list[int], start_index: int = 0, end_index: int = None
) -> tuple[int, int]:
    highest_digit = 0
    found_index = 0
    if end_index is None:
        end_index = len(digits)
    for i, d in enumerate(digits[start_index:end_index]):
        if d == 9:
            return i, d
        if d > highest_digit:
            highest_digit = d
            found_index = i
    return found_index, highest_digit


def solve_part_1_two_passes(data: list[str]) -> int:
    joltages = []
    for line in data:
        digits = [int(digit) for digit in str(line)]
        # find highest number you can make via a pair of digits
        found_index, first_digit = get_highest_number_in_range(
            digits=digits, end_index=len(digits) - 1
        )
        _, second_digit = get_highest_number_in_range(
            digits=digits, start_index=found_index + 1
        )
        joltages.append(int(str(first_digit) + str(second_digit)))
    return sum(joltages)


def get_highest_joltage_part_1(digits: list[int]) -> int:
    max_seen = 0
    highest_joltage = 0
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i]
        candidate = d * 10 + max_seen
        if i != len(digits) - 1 and candidate > highest_joltage:
            highest_joltage = candidate
        if d > max_seen:
            max_seen = d
    return highest_joltage


def solve_part_1_one_pass(data: list[str]) -> int:
    joltages = []
    for line in data:
        digits = [int(digit) for digit in str(line)]
        joltages.append(get_highest_joltage_part_1(digits))
    return sum(joltages)


def solve_part_2(data: list[str]) -> int:
    joltages = []
    for line in data:
        digits = [int(digit) for digit in str(line)]
        tracked_index = 0
        joltage_digits = []
        for k in range(12):
            end_index = len(digits) - 11 + k
            new_index, d = get_highest_number_in_range(
                digits, start_index=tracked_index, end_index=end_index
            )
            # move the collective index
            # range returns the index of the range instead of the full list
            tracked_index += new_index + 1
            joltage_digits.append(d)
        joltages.append(int("".join(map(str, joltage_digits))))
    return sum(joltages)


def main():
    data = read_data("data.txt")
    # print("Part 1: ", solve_part_1_one_pass(data))
    print("Part 2: ", solve_part_2(data))


if __name__ == "__main__":
    main()
