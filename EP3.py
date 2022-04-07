"""
การใช้ for ที่น่าสนใจ
"""



x = int(input("เลขมา 1 จำนวน >>>"))

if x <10:
    for i in range(1,5):
        x += 2
        if x % 2 ==  0:
            print(x)

