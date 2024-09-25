import bisect


def calculate_spin_multiplier(spins):
    variables = [1, 2, 3, 5, 10, 50, 150, 1000]
    idx = bisect.bisect_right(variables, spins) - 1

    return 1
