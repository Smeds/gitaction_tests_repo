def hello_world():
    """Print hello world and return 1.

    >>> hello_world()
    hello world
    1
    """
    print("hello world")
    return 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
