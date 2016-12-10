"""A function to convert list of ones and zeros to that binary zalue's equivalent integer."""


def binary_list_to_number(arr):
    """Convert list of ones and zeros to that binary zalue's equivalent integer."""
    numb = 0
    for i in range(len(arr)):
        numb += arr[-(i + 1)] * 2**(i)
    return numb
