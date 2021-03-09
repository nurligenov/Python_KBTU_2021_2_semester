#https://informatics.mccme.ru/mod/statements/view.php?id=4163#1
# arr=list(map(int,input().split()))
# for i in range(0,len(arr),2):
#     print(arr[i],end=" ")

#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3835#1
# arr=list(map(int,input().split()))
# mi=1000000000
# for i in arr:
#     if i>0:
#         mi=min(mi,i)
# print(mi)

#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3840#1
# arr=list(map(int,input().split()))
# print(*reversed(arr))

#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1
# arr=list(map(int,input().split()))
# c=0
# for i in arr:
#     if i!=0:
#         print(i,end=" ")
#     else:
#         c=c+1
# for i in range(c):
#     print(0,end=" ")

#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3853#1
# arr=list(map(int,input().split()))
# k=int(input())
# arr=arr[-(k%len(arr)):]+arr[:-(k%len(arr))]
# print(*arr)

#https://informatics.mccme.ru/mod/statements/view.php?id=4535#1
# print(len(set(list(map(int,input().split())))))

# https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3750#1
# s=list(set(list(map(int,input().split()))))
# ss=list(set(list(map(int,input().split()))))
# r=s+ss
# print(len(r)-len(set(r)))

#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3751#1
# print(*sorted(list(set(list(map(int,input().split()))).intersection(set(list(map(int,input().split())))))))

#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3753#1
# from collections import defaultdict
# di={}
# di=defaultdict(lambda:0,di)
# while True:
#     arr=list(map(str,input().split()))
#     for s in arr:
#         di[s]=di[s]+1
# arr=[]
# for key in di:
#     arr.append((-di[key],key))
# arr.sort()
# for i in arr:
#     print(i[1])

#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3774#1
class Node:
    def __init__(self):
        self.parents=[]
        self.children=0
z=Node()
n=int(input())
arr=[]
for _ in range(n-1):
    x,y=map(str,input().split())
    arr.append(x)
    arr.append(y)
    if type(x)!=type(z):
        x=Node()
    if type(y)!=type(z):
        y=Node()
    x.parents.append(y)
    y.children=y.children+1
    for i in y.parents:
        x.parents.append(i)
        i.children=i.children+1
arr=list(set(arr))
print(arr)
print(arr[0].parents)



