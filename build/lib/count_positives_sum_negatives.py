"""A function to return an array of the count of positive elements and the sum of negative elements in an input array."""


def count_positives_sum_negatives(arr):
    """Return an array of the count of positive elements and the sum of negative elements in an input array.."""
    sums_pos = 0
    sums_neg = 0
    if len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            sums_pos += 1
        else:
            sums_neg += i
    return [sums_pos, sums_neg]
