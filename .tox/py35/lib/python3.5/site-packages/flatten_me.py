"""A function to flatten a list of lists or return an already flat list."""


def flatten_me(lst):
    """Flatten a list of lists or return an already flat list."""
    n_lst = []
    for i in lst:
        try:
            for j in i:
                n_lst.append(j)
        except:
            n_lst.append(i)
    return n_lst
