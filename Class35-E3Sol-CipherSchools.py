name,ch= input("Enter Comma Seperated Name and character: ").split(",")
print(f'Length of your name: {len(name)}')

#! Case Sensitive
print(f'Sens Character Count: {name.count(ch)}')
#! Case Insensitive
#*Suphal - suphal
#*S  - s
name = name.lower()
ch=ch.lower()
print(f'InSens Character Count: {name.count(ch)}')
#! Space remove strip()
#^ "       Suphal    "--------->    "Suphal"      --------->      "suphal"
#^ "     S      "------->   "H"   --------->   "h"

print(f'Space1 Character Count: {name.replace(" ","").lower().count(ch.replace(" ","").lower())}')
print(f'Space2 Character Count: {name.strip().lower().count(ch.strip().lower())}')

