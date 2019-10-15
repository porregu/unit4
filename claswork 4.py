import random


b=(float(input("what number you choose between 1 and 3")))# user decision


def game():

    """
    is the game of rock paper scissors
    :return:
    """
# 1= rock 2= paper 3= sccissors
    a = random.randint(1, 3) # machine decision
    print(a)
    if a==1 and b==2:
        print("b win")
    if a==b:
        print("tie")
    if a==2 and b==3:
        print("b won ")
    if a==1 and b==3:
        print("a won")
    if a==2 and b==1:
        print("a won")

game()