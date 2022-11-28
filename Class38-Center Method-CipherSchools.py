
name="Suphal"
#^ to print **Suphal**  len=10
#! Syntax:- variable.center(len of expected output,"to be printed extra") 
print(name.center(10,"!"))
print(name.center(9,"@"))
print(name.center(7,"*"))


nam=input("Enter your name: ")
ch=input("enter the character you want to input: ")
no=int(input("Enter the no of times the char should apply: "))
print(nam.center((len(nam)+no), ch))
