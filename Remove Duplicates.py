n = int(input("How many Iteams You Want to Add to the List :"))
list1 = []
for i in range(0, n):
    a = int(input())
    list1.append(a)

for j in list1:
    if( list1.count(list1[j - 1])  > 1):
        list1.remove(list1[j - 1])

print(list1)