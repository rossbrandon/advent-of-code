START_POSITION = 50
DIAL_LENGTH = 100


def read_data(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()


def parse_line(line: str) -> tuple[str, int]:
    return line[0], int(line[1:])


def rotate_dial(position: int, direction: str, distance: int) -> int:
    if direction == "L":
        return (position - distance) % DIAL_LENGTH
    elif direction == "R":
        return (position + distance) % DIAL_LENGTH
    else:
        raise ValueError(f"Invalid direction: {direction}")


def solve_part_1(data: list[str]) -> int:
    position = START_POSITION
    zero_count = 0
    for line in data:
        direction, distance = parse_line(line)
        position = rotate_dial(position, direction, distance)
        if position == 0:
            zero_count += 1
    return zero_count


def get_distance_to_zero(position: int, direction: str) -> int:
    if direction == "L":
        return position or DIAL_LENGTH
    elif direction == "R":
        return DIAL_LENGTH - position
    else:
        raise ValueError(f"Invalid direction: {direction}")


def solve_part_2(data: list[str]) -> int:
    position = START_POSITION
    zero_count = 0
    for line in data:
        direction, distance = parse_line(line)
        distance_to_zero = get_distance_to_zero(position, direction)
        if distance >= distance_to_zero:
            zero_count += 1 + (distance - distance_to_zero) // DIAL_LENGTH
        position = rotate_dial(position, direction, distance)
    return zero_count


def main():
    data = read_data("data.txt")
    print("Part 1 Password: ", solve_part_1(data))
    print("Part 2 Password: ", solve_part_2(data))


if __name__ == "__main__":
    main()
