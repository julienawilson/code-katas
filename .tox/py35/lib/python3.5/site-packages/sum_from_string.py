"""A function to sum numbers found in a string."""


def sum_from_string(string):
    """Sum numbers found in a string."""
    new_l = []
    for i in list(string):
        try:
            int(i)
            new_l.append(i)
        except:
            new_l.append(" ")
    nums = []
    for i in "".join(new_l).split():
        nums.append(int(i))
    return sum(nums)
