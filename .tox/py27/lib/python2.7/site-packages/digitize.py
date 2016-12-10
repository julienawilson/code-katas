"""A function to convert a number to a reversed array of digits."""


def digitize(n):
    """Convert a number to a reversed array of digits."""
    l = list(str(n))
    n_l = []
    for d in l:
        n_l.append(int(d))
    n_l.reverse()
    return n_l
