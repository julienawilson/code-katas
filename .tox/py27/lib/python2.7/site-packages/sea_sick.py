"""A function to convert a string to an array of words."""


def sea_sick(sea):
    """getin sick."""
    sick = 0
    for i in range(len(sea) - 1):
        if sea[i] != sea[i + 1]:
            sick += 1
    if sick > len(sea) * .2:
        return "Throw Up"
    return "No Problem"
