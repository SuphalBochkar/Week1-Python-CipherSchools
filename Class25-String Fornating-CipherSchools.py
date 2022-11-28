# Sting formating

name , age = input("enter your name and age ").split(" ")

print("hello {} your age is {}".format(name,int(age)+3))              #!Python 3

print(f"hello {name} your age is {age}")                                    #!best

print(f"hello {name} your age is {int(age)+2}") 

print("hiii %s your age is %s" ,name , age)






