# -*- coding: utf-8 -*-

try:
    age = int(input("age: "))
    age = 10/age
    raise ValueError("Ending the program")
    # raise Exception("quit")

except ValueError:
    print("Please enter a no.")