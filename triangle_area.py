def area(a, b, c):
    """
    :param x:
    :param y:
    :return:
    """
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    return area

