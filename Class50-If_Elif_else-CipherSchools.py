a=int(input("Age? : "))



if a==0:
    print("No Entry")
elif 0<a<=10:
    print("Ticket Price : Free")
elif 3<a<=10:
    print("Ticket Price : 100")
elif 10<a<=60:
    print("Ticket Price : 150")
else:
    print("Ticket : 200")