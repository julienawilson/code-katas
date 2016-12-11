"""A function to find the sum of the first nth terms of a series 1+1/4+1/7+..."""


def series_sum(n):
    """Find the sum of the first nth terms of a series 1+1/4+1/7+..."""
    total = 0
    for i in range(n):
        total += 1.0 / (1 + i * 3)
    return "%.2f" % total
 