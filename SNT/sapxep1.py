print("Chương trình in ra các số chẵn trong mảng bằng Python")
print("Gõ exit để thoát chương trình")

def in_so_chan(listNum):
    """Hàm in ra các số chẵn một mảng"""
    for i in listNum:
        if i % 2 == 0:
            print(i, end=' ')


# Chương trình chính
listNum = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
in_so_chan(listNum)