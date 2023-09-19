# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""Purpose: Practice digits and while loops

Problem Statement:
Given an integer greater than 9, print the number created by reversing the digits, 1's value first,
 and then 10's value and then the 100's value, and so on, as a number."""

number = int(input("write a number"))
i = 1
while i <= len(str(number)):
    print((number % 10**i)//10**(i-1), end="")
    i = i+1

