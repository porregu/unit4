import random

def po(speed,birthday):
    if birthday==True:
        speed-=5
    if speed<=60:
        return 0
    if speed>=61 and speed<=80:
        return 1
    if speed>=81:
        return 2

print(po(60,False))
print(po(65,False))
print(po(65,True))