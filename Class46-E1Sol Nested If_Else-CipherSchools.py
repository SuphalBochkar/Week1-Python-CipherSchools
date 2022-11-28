import random
w_n=18
n=int(input("Enter the number: "))
if w_n==n:
    print("You Win")
else:
    #! 1.
    if n < w_n:
        print("Its Too low")
    else :                                               #! Nested If-Else
        print("Its Too high")

    #! 2.
    if n>w_n:                                            #! Nested If-Else
        print("Its Too high")

        
