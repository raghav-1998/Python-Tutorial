"""
Write a Python program that displays a message as follows for a given number:

- If it is a multiple of 3, display "Zip"

- If it is a multiple of 5, display "Zap"

- If it is a multiple of both 3 and 5, display "Zoom"

- If it does not satisfy any of the above given conditions, display "Invalid"
"""


def selection_demo(n):
    if(n%3==0 and n%5==0):
        print("Zoom")
    
    elif(n%3==0):
        print("Zip")
    
    elif(n%5==0):
        print("Zap")
    
    else:
        print("Invalid")


if __name__=="__main__":
    n=int(input())
    selection_demo(n)