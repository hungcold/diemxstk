def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;


n = int(input("Nhập số nguyên dương n = "));
if (n >= 0):
    print("Không phải số nguyên dương, vui lòng nhập lại!")
else:
    n = int(input("Nhập số nguyên dương n = "));
print("Giai thừa của", n, "là", tinhgiaithua(n));