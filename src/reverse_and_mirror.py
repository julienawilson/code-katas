"""A function to concatonate a reversed swapcased string with a mirrored swapcased string."""


def reverse_and_mirror(s1, s2):
    """Concatonate a reversed swapcased string with a mirrored swapcased string."""
    new_string = ""
    new_s2 = s2[::-1].swapcase()
    new_s1 = s1[::-1].swapcase() + s1[::].swapcase()
    new_string += new_s2 + "@@@" + new_s1
    return new_string
