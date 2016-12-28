"""Ensure the same number of opening and closing parenthetics in a string."""

from stack import Stack


def proper_parenthetics(input_string):
    """Ensure the balance of opening and closing parenthtics."""
    parenthetics_stack = Stack()
    for i in input_string:
        if i == '(':
            parenthetics_stack.push(i)
        if i == ')':
            if parenthetics_stack.head_node is None:
                return -1
            parenthetics_stack.pop()
    if parenthetics_stack.head_node is None:
        return 0
    return 1
