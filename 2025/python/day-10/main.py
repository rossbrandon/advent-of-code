import time
from itertools import product

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def parse_line(line: list[str]) -> tuple[list[int], list[list[int]], list[int]]:
    lights_str = line[line.index("[") + 1 : line.index("]")]
    target = [1 if c == "#" else 0 for c in lights_str]
    button_section = line[line.index("]") + 1 : line.index("{")]
    buttons = []
    for c in button_section.split("(")[1:]:
        nums = c.split(")")[0]
        buttons.append([int(num) for num in nums.split(",")])

    joltage_str = line[line.index("{") + 1 : line.index("}")]
    joltage = [int(num) for num in joltage_str.split(",")]

    return target, buttons, joltage


def read_data(path: str) -> list[list[int]]:
    with open(path, "r") as file:
        return [parse_line(line) for line in file.read().strip().split("\n")]


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def min_presses(target: list[int], buttons: list[list[int]]) -> int:
    n_lights = len(target)
    n_buttons = len(buttons)
    min_presses = float("inf")

    for combo in product([0, 1], repeat=n_buttons):
        light_state = [0] * n_lights

        # apply the button presses
        for btn_idx, pressed in enumerate(combo):
            if pressed:
                for light_idx in buttons[btn_idx]:
                    light_state[light_idx] ^= 1  # XOR

        # check if the light state matches the target state
        if light_state == target:
            min_presses = min(min_presses, sum(combo))

    return min_presses


def solve_part_1(data: list[list[int]]) -> int:
    return sum(min_presses(target, buttons) for target, buttons, _ in data)


def min_joltage_presses(joltage: list[int], buttons: list[list[int]]) -> int:
    n_counters = len(joltage)
    n_buttons = len(buttons)

    # build matrix: A[counter][button] = 1 if button affects counter, 0 otherwise
    A = np.zeros((n_counters, n_buttons))
    for btn_idx, btn in enumerate(buttons):
        for counter_idx in btn:
            if counter_idx < n_counters:
                A[counter_idx, btn_idx] = 1

    # minimize the sum of the presses
    c = np.ones(n_buttons)
    # constraints: A @ x == joltage
    constraints = LinearConstraint(A, joltage, joltage)
    # x >= 0
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)

    # solve milp
    result = milp(c, integrality=integrality, constraints=constraints, bounds=bounds)
    return int(result.fun)


def solve_part_2(data: list[list[int]]) -> int:
    return sum(min_joltage_presses(joltage, buttons) for _, buttons, joltage in data)


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
