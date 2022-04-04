"""
การใช้ for ที่น่าสนใจ
"""
base = float(input("เลขฐาน>>>"))
power = int(input("เลขยกกำลัง (เป็นจำนวนเต็ม)>>>"))

if power >= 0:
    result = 1
    for i in range(0,power):
        print(i)
        result *= base


print(result)