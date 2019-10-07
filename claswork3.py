def main():
    """

    :return: to the equation
    """
    A = (float(input("what is your fist number")))# first side of the triangle
    B = (float(input("what is your second number"))) # second side of the triangle
    C = (float(input("what is your third numeber"))) # third side of the triangle
    if (A+B==C): # equation for the triangle
        print("it's a degenerated triangle")
    else:
        print("is not a degenerated triangle")

main()