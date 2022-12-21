# 8.  Given the sets below, write python statement to: 
#     Set1= {1, 2, 3, 4, 5} 
#     Set2= {2, 4, 6, 8} 
#     Set3= {1, 5, 9, 13, 17} 
#     a.  Create a new set of all elements that are in Set1 and Set2 but not both. 
#     b.  Create a new set of all elements that are in only one of the three sets Set1, 
#         Set2 and Set3. 
#     c.  Create a new set of elements that are exactly two of the sets Set1, Set2 
#         and Set3. 
#     d.  Create a new set of all integers in the range 1 to 10 that are not in Set1. 
#     e.  Create a new set of all integers in the range 1 to 10 that are not in Set1, 
#         Set2 and Set3. 

s1= {1, 2, 3, 4, 5}
s2= {2, 4, 6, 8}
s3= {1, 5, 9, 13, 17}

# a.
sa = s1.intersection(s2)

print("\nElements that are in set1 and set2:", sa)

# b.
sb1_1 = s1 - s1.intersection(s2)
sb1_2 = sb1_1  - sb1_1.intersection(s3)

sb2_1 = s2 - s2.intersection(s1)
sb2_2 = sb2_1  - sb2_1.intersection(s3)

sb3_1 = s3 - s3.intersection(s1)
sb3_2 = sb3_1  - sb3_1.intersection(s2)

sb = sb1_2.union(sb2_2).union(sb3_2)

print("\nElements only one of the three sets Set1, Set2 and Set3:", sb)

# c.
sc1_1 = s1.intersection(s2)
sc1_2 = sc1_1 - sc1_1.intersection(s3)

sc2_1 = s2.intersection(s3)
sc2_2 = sc2_1 - sc2_1.intersection(s1)

sc3_1 = s3.intersection(s1)
sc3_2 = sc3_1 - sc3_1.intersection(s2)

sc = sc1_2.union(sc2_2).union(sc3_2)

print("\nElements that are exactly two of the sets Set1, Set2 and Set3:", sc)

# d.
sd = set()
for i in range(1, 11):
    if i in s1:
        continue
    else:
        sd.add(i)

print("\nSet of all integers in the range 1 to 10 that are not in Set1:", sd)

# e.
su = s1.union(s2).union(s3)
se = set()
for j in range(1, 11):
    if j in su:
        continue
    else:
        se.add(j)

print("\nSet of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:", se,"\n")