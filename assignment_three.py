print("This program calculates the surface area of a rectangular prism")
def get_width():
    """
    Asks for a length then returns the answer as the function
    :return:
    """
    x = input("What is the width")
    return float(x)
def get_height():
    """
    Asks for a length then returns the answer as the function
    :return:
    """
    y = input("What is the height")
    return float(y)
def get_length():
    """
    Asks for a length then returns the answer as the function
    :return:
    """
    z = input("What is the length")
    return float(z)
def rectangle_area(x, y):
    side_area = x * y
    return side_area
def calculate_surface_area(x, y , z):
    """
    calculates all the surface areas then adds them. Spits out the answer as calculate_surface_area
    :param x:
    :param y:
    :param z:
    :return:
    """
    side1and2 = rectangle_area(x, y)* 2
    side3and4 = rectangle_area(x, z) * 2
    side5and6 = rectangle_area(y, z) * 2
    total = side1and2 + side3and4 + side5and6
    return total

def reply(x, y, z, total):
    print("Surface area of a rectangular prism with a width of", x, ",height of", y, ", and length of", z, "is", total)

def main():
    """
calls all of the functions then replies to the person
also assigns functions a value
    :return:
    """
    x = get_width()
    y = get_height()
    z = get_length()
    total = calculate_surface_area()
    reply(x, y, z, total)

if __name__ == '__main__':
    main()