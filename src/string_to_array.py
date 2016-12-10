"""A function to convert a string to an array of words."""


def string_to_array(string):
    """Convert a string to array, even if empty."""
    if string == "":
        return [""]
    return string.split()
