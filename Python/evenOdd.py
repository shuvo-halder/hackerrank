#! /bin/python3

import os
import math
import sys
import re
import random


def checkOdd(number):
    checkOddRes = (number % 2) == 1
    return checkOddRes;

def checkWeirdOrNot(numb):
    if checkOdd(numb):
        print('Weird')
    elif 2 <= numb <= 5:
        print('Not Weird')
    elif 6 <= numb <= 20:
        print("Weird")
    elif numb > 20:
        print("Not Weird")


if __name__ == '__main__':
    numb = int(input('Enter Number: ').strip())
    checkWeirdOrNot(numb)
