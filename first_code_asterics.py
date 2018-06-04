

"""Add two numbers"""


def add_number(a,b):
    """ Add two numbers

    Args:
        a (complex): first number
        b (complex): second number
        add_answer: add the answer to life, universe and everything

    Returns:
        their sum
    """
    result = a + b
    answer_to_the_universe = 42
    # if add_answer:
    #     result += answer_to_the_universe
    return result


if __name__ == '__main__':
    print(add_number(3, 5))
    print(add_number("a", "b"))
    print(add_number.__annotations__)