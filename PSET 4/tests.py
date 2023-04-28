import unittest

from tastiest_slice import tastiest_slice

tests = (
    (
        [(-7, 8, 5), (2, -4, 3), (7, 10, -1), (4, -3, 9), (-5, 1, 9)],
        (4, 8, 26),
    ),
    (
        [
            (15, -1, 0),
            (7, 11, -7),
            (20, -8, 9),
            (-16, -4, 13),
            (0, -11, 18),
            (19, -13, -8),
            (16, 1, -14),
            (-14, -3, 10),
            (-7, 13, 1),
            (6, -10, 17),
        ],
        (6, 13, 59),
    ),
    (
        [
            (3, 11, 30),
            (-25, -8, 16),
            (-21, 6, 31),
            (-3, 20, -3),
            (-9, -22, 8),
            (-24, 19, -23),
            (-7, -20, 11),
            (7, 27, 29),
            (-14, 22, -24),
            (24, 21, 11),
            (-17, 12, -24),
            (16, -13, 28),
            (-26, -27, -3),
            (-1, 29, -4),
            (-16, -29, -19),
        ],
        (16, 11, 102),
    ),
    (
        [
            (-41, 5, -4),
            (-43, 50, -1),
            (-19, -42, -32),
            (-34, 34, 30),
            (28, -5, -10),
            (14, -29, 21),
            (-31, -27, -8),
            (0, -48, -21),
            (44, -32, 19),
            (-3, 19, 8),
            (8, -35, -23),
            (22, 36, -21),
            (-49, -16, 31),
            (49, 15, 6),
            (-40, -13, 2),
            (2, -9, 43),
            (47, 3, 35),
            (-44, 45, 21),
            (17, 18, -10),
            (-50, -26, 7),
            (-10, -47, -14),
            (-2, 39, -27),
            (-36, -8, 2),
            (-25, -7, -13),
            (-1, -6, -27),
        ],
        (-34, 45, 89),
    ),
    (
        [
            (-12, 83, 11),
            (-16, -74, -74),
            (-17, -25, -60),
            (-21, -69, -64),
            (-22, 94, -42),
            (-23, 53, 49),
            (-27, 97, 35),
            (-3, -87, 45),
            (-33, 39, 3),
            (-37, -19, -58),
            (-38, -89, 5),
            (-39, 19, -77),
            (-41, 78, 53),
            (-51, 33, 100),
            (-52, 35, 91),
            (-57, 12, 13),
            (-66, -31, 31),
            (-67, 11, -75),
            (-68, -94, -35),
            (-73, 28, -53),
            (-76, 25, -76),
            (-79, 26, 47),
            (-86, 66, -24),
            (-92, 2, -42),
            (-96, -65, 66),
            (-98, 96, 76),
            (0, 50, -61),
            (1, 45, 53),
            (10, -63, 98),
            (17, -70, 36),
            (18, -62, -12),
            (23, -85, 59),
            (24, -36, 55),
            (3, -90, -76),
            (32, -34, 33),
            (36, -81, -4),
            (44, 34, -8),
            (46, 92, -73),
            (47, -93, 49),
            (54, 81, 88),
            (55, 7, 0),
            (58, 22, -26),
            (62, -82, -17),
            (63, -30, 36),
            (71, 69, 16),
            (72, -45, -11),
            (76, -61, 81),
            (9, -1, 13),
            (95, 75, -3),
            (98, -75, -46),
        ],
        (76, -30, 301),
    ),
    # My own test case demonstrating simple example
    # of when given solution code fails
    (
        [(-7, 8, 5), (-2, -2, 3), (-2, -7, -100)],
        (-7, 8, 5),
    ),
)


def check(test):
    args, staff_sol = test
    _, _, T = staff_sol
    toppings = [x for x in args]
    X, Y, T_ = tastiest_slice(toppings)
    if T != T_:
        print(f"\ncorrect result: {T}")
        print(f"tastiest_slice result: {T_}")
        return False
    T_ = 0
    for x, y, t in args:
        if x <= X and y <= Y:
            T_ += t
    return T == T_


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))

    # BUG: The tastiest slice actually depends on order of toppings
    # sorted by y coordinates for toppings sharing an x-coordinated!
    def test_06(self):
        self.assertTrue(check(tests[5]))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
