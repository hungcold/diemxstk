A=[1,1,2,3,5,8,13,21,34,55,88]
B=[1,3,5,4,7,88,66,59,40,54]
C = set(A) & set(B)
print("Các phần tử trùng nhau trong list A,B là",C)
for i in A:
    for j in B:
        if(j==i):
            A.remove(j)
            B.remove(j)
print("Xóa các phần tử trong list A bị trùng nhau",A)
print("Xóa các phần tử trong list B bị trùng nhau",B)