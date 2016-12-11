"""A function to find the last item of an iterable."""


def last(*args):
    """Find the last item of an iterable or series of inputs."""
    if len(args) > 1:
        l = list(args)
        return l[-1]
    if type(args[-1]) is int:
        return args[-1]
    return list(args[0])[-1]
