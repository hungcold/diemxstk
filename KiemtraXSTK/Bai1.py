list = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
list2=[]
for i in list:
    if i < 30:
        list2.append(i)
        print("Các số nhỏ hơn 30 là:",list2)
n = int(input('Nhập vào một số:'))
list3=[]
for j in list:
    if (n < j):
        list3.append(j)
        print("Các số lơn hơn", n, "là:",j)

