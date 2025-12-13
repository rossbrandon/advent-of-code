import time
from collections import Counter
from math import dist


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


def read_data(path: str) -> list[list[int]]:
    with open(path, "r") as file:
        data = file.read().strip().split("\n")
        return [list(map(int, line.split(","))) for line in data]


def get_elapsed_time(start_time: float, end_time: float) -> float:
    return (end_time - start_time) * 1000


def find_pairs(data: list[list[int]]) -> list[tuple[int, int, int]]:
    pairs = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            # calculate the Euclidean distance between the two points
            distance = dist(data[i], data[j])
            pairs.append((distance, i, j))
    pairs.sort()
    return pairs


def connect_circuits(uf: UnionFind, pairs: list[tuple[int, int, int]], max: int):
    for _, i, j in pairs[:max]:
        uf.union(i, j)


def solve_part_1(data: list[list[int]], max_connections: int) -> int:
    # find the pairs of junction boxes that are closest together
    pairs = find_pairs(data)
    # track which junction boxes are in the same circuit via a union find
    uf = UnionFind(len(data))
    # connect the circuits (10 for test, 1000 for real data)
    connect_circuits(uf, pairs, max_connections)
    # find which junction boxes each circuit belongs to (it's root)
    roots = [uf.find(i) for i in range(len(data))]
    # count the number of junction boxes in each circuit
    boxes_in_circuits = Counter(roots)
    # sort the circuit sizes, largest to smallest
    circuit_sizes = sorted(boxes_in_circuits.values(), reverse=True)
    # multiply the three largest circuit sizes
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def solve_part_2(data: list[list[int]]) -> int:
    pairs = find_pairs(data)
    uf = UnionFind(len(data))
    # track the last successful connection
    last_i, last_j = 0, 0
    connections = 0
    for (
        _,
        i,
        j,
    ) in pairs:
        if uf.union(i, j):
            last_i, last_j = i, j
            connections += 1
            # break after connecting all the boxes
            if connections == len(data) - 1:
                break
    # multiply the x coordinates of the last two junction boxes we need to connect
    return data[last_i][0] * data[last_j][0]


def main():
    data = read_data("data.txt")

    # Part 1
    start_time = time.perf_counter()
    part_1 = solve_part_1(data, max_connections=1000)
    end_time = time.perf_counter()
    print(f"Part 1: {part_1} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")

    # Part 2
    start_time = time.perf_counter()
    part_2 = solve_part_2(data)
    end_time = time.perf_counter()
    print(f"Part 2: {part_2} - Took: {get_elapsed_time(start_time, end_time):.2f}ms")


if __name__ == "__main__":
    main()
