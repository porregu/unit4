import random

X = (float(input("what you want to be the maximun ")))# ask the user for the maximun number that the user wants
def problem():
    """

    :return: this makes the user choose a type of problema and the maximun number he want starting for 0, then the computer will choose two random numbers and the user need to put his answer for the problem and the cmputer will solve it and tell if is correct or not.
    """
    a =random.randint(0,X)# computer choose a random number
    b =random.randint(0,X)# computer choose a random number
    D=(input("what time of problem you want addition (+) subtraction (-) or multiplication (*)"))
    if D != "*" and D != "-":# check the problems that the user choose
        D="+"
    answer=int (input ("what is"+str(a)+D+str(b)))# make the equation for the problems
    if D =="*":
        correct=a*b# is the correct answer to compare later with user choice
        if answer==correct:
            (print("right"))
        if answer!=correct:
            (print("wrong"))
            (print(a*b,"is the correct answer"))
    if D =="-":
        f=a-b
        if answer==f:
            (print("right"))
        if answer!=f:# is the correct answer to compare later with user choice
            (print("wrong"))
            print(a-b,"is the correct answer")

    if D!="*" and D!="-":
        O=a+b# is the correct answer to compare later with user choice
        if answer==O:
            (print("right"))
        if answer!=O:
            (print("wrong"))
            print(a+b,"is the correct answer")

problem()