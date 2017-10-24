#!/bin/env

number = int(input("Insert a number: "))
while (number != 1):
    print(number, ", ", end='')
    if (number % 2 == 0):
        number = int(number / 2)
    else:
        number *= 3
        number += 1
print(number)
exit()
