import random

X = (float(input("what you want to be the maximun ")))
def problem():
    a =random.randint(0,X)
    b =random.randint(0,X)
    D=(input("what time of problem you want addition (+) subtraction (-) or multiplication (*)"))
    if D != "*" and D != "-":
        D="+"
    answer=int (input ("what is"+str(a)+D+str(b)))
    if D =="*" >a*b==answer:
        print("right")
        if D =="-" > a+b==answer:
            if  a-b==answer:
                print("right")
    else:
        print("wrong")



problem()



