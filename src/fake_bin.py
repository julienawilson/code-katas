"""A function to convert a string of numbers to a string of binary."""


def fake_bin(x):
    """Convert a string of numbers to a string of binary."""
    l = list(x)
    new_l = []
    for digit in l:
        if int(digit) <5:
            new_l.append("0")
        else:
            new_l.append("1")
    return "".join(new_l)
