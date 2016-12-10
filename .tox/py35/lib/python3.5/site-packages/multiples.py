"""A function to show multiples of two numbers within a given range.."""


def multiples(s1, s2, s3):
    """Show multiples of two numbers within a given range."""
    result = []
    for i in range(s3):
        if i % s1 == 0 and i % s2 == 0 and i:
            result.append(i)
    return result
