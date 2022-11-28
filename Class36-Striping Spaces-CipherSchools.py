# Striping the spaves


dot="...................."
name="         Suphal           "
dots="......................."
# lstrip()   Method
print(dot+name+dots)
print(dot+name.lstrip()+dots)
# rstrip()  Method
print(dot+name.rstrip()+dots)
# rstrip() and lstrip()  Method   or strip()
print(dot+name.lstrip().rstrip()+dots)
print(dot+name.strip()+dots)
print(dot+name.replace(" ","")+dots)

# ! To remove all spaces
a="Suu   P h  jk   ljk  kh "
print(a.replace(" ",""))




