import sys
import os
import math

def pythonDivision(firstNumber, secondNumber):
    integerDiv = firstNumber // secondNumber
    floatDiv = firstNumber / secondNumber
    print(integerDiv)
    print(floatDiv)

if __name__ == "__main__":
    firstNumber = int(input())
    secondNumber = int(input())
    pythonDivision(firstNumber,secondNumber)
