# This is a sample Python script.
"""Problem Statement: Determine if a string entered by the user is a palindrome or not. A palindrome is a
string that is the same from left to right and right to left. Assume all entries are lowercase."""

"""
understanding:
input= a string
output= true if the string is palindrome or false is the string is not palindrome

match:
backward loop, if else statements, palindrome exercise 

plan:
1. input a string
2. create a variable called front=0, and create a variable called end=len(string)-1
3. create a for loop in the range of the length of the string
   3.1 check if front is different form end
       3.2 if it is different the break the loop
          3.3 print false 
4. else increment front+1 and decrement   the end -1 
5. if front is greater than end 
  5.1 print true.
  
implementation:     
"""
word = (input("write a word "))
front = 0
end = len(word)-1
for i in range(len(word)):
    if word[front] != word[end]:
        print("false")
        break
    else:
        front = front+1
        end = end-1
        if front > end:
            print("true")
            break








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
