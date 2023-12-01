from functools import cache


def split_bowling(pins: list[int]) -> int:

    @cache
    def x(remaining_pins: tuple[int]) -> int:
        if not remaining_pins:
            return 0
        best = 0
        for i, _ in enumerate(remaining_pins):
            local_best = max(
                remaining_pins[i] + x(tuple(remaining_pins[:i] + remaining_pins[i+1:])),
                (remaining_pins[i] * remaining_pins[i+1]) + x(tuple(remaining_pins[:i] + remaining_pins[i+2:])) if 0 <= i+1 < len(remaining_pins) else 0,
                x(tuple(remaining_pins[:i] + remaining_pins[i+1:]))
            )
            best = max(best, local_best)
        return best

    return x(tuple(pins))

# 7 elements = 7 choose 7
# 6 element = 7 choose 6
# 5 elements = 7 choose 5
# ...



if __name__ == "__main__":
    test1 = [-22, 57, 1, 3, 4, -7, -2]
    test2 = [-4, 4, 4, -4]
    test3 = [-7, 2, 1, -19, -3, -4, -10]
    assert split_bowling(test1) == 386
    assert split_bowling(test2) == 32
    assert split_bowling(test3) == (190 + 12 + 3) 
    print(split_bowling(test1))
    print(split_bowling(test2))
    print(split_bowling(test3))
    