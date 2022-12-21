# 6.  Write  a  python  script  that  repeatedly  ask  user  to  enter  name  and  SID  of 
#     students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and 
#     values are student’s name. Perform the following operations on Dictionary : 
#     a.  Print students details stored in the dictionary. 
#     b.  Sort dictionary using student names. 
#     c.  Sort dictionary using SID. 
#     d.  Search a student details with SID and print name of that student.

from collections import OrderedDict

i = "Y"
dict0 = {}

while(i=="Y"):
    sid = input("Enter Your Sid: ")
    name = input("Enter Your Name: ")
    dict0.update({sid:name})
    print("\nStudent added successfully\n")
    i = input("To add a new student, enter Y\nTo move forward, enter N\n")

# a.
print("Student Details: ", dict0)

# b.
k = list(dict0.keys())
lk = len(k)
v = list(dict0.values())
lv = len(v)

i = 0

dict_rev = {}
while i<lk:
    dict_rev.update({v[i]:k[i]})
    i = i+1

dict_rev1 = OrderedDict(sorted(dict_rev.items()))


k2 = list(dict_rev1.keys())
lk2 = len(k2)
v2 = list(dict_rev1.values())
lv2 = len(v2)

j = 0

dict2 = {}
while j<lk2:
    dict2.update({v2[j]:k2[j]})
    j = j+1

print("\nSorted using names: ", dict2)

# c.
dict3 = OrderedDict(sorted(dict0.items()))
dict3 = dict(dict3)
print("\nSorted using SID's: ", dict3)

# d.
search = input("\nEnter SID to search name\n")
if search in list(dict0.keys()):
    print(f"{search} : {dict0[search]}")
else:
    print("SID not found!")