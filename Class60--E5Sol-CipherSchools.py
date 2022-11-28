name=str(input("Enter the name: "))
i=0


# temp=""

# while i< len(name):
#     if  name[i] != temp:
#         temp = name[i]
#         print(f"{name[i]} : {name.lower().count(name[i].lower())}")
#     i+=1


temp_var = ""
j=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    j+=1
    
    
    
