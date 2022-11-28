# Find And Replace


sen="She is beautiful and she is good dancer"
print(sen.replace(" ","_"))
# replace how many characters  present
print(sen.replace("is","was",1))
print(sen.replace("is","was",2))

# Find Position
print(sen.find("is"))          #!its index value
# finding frm cirtain position
print(sen.find("is",2))
# if u want other but 1st is showing
is_po1=sen.find("is")           #Know first one then add it in to find second one
print(sen.find("is",is_po1+1))


