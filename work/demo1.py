#!/usr/bin/env python

def displayNumType(num):
    print(num,"is")
    if(isinstance(num,(int,float,complex))):#是否在这些类型之中
        print("a numebr of type:", type(num).__name__)
    else:
        print("not a number at all!!")

displayNumType(-69)
displayNumType(99999999999999999999)
displayNumType(98.6)
displayNumType(-5.2+1.9)
displayNumType('xxx')