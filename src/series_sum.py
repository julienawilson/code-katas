"""A function to find the sum of the first nth terms of a series 1+1/4+1/7+..."""


def series_sum(n):
    """Find the sum of the first nth terms of a series 1+1/4+1/7+..."""
    sum = 0
    for i in range(n):
        sum += float(1 / (1 + i * 3))
    return str("%.2f" % sum)
