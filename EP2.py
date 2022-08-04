"""
การออกเบบการใช้ for ร่วมกับ if
"""


sum = 0
for i in range(1,5):
    num = int(input(f"จำนวนเงินที่ {i} >>>")) # การใช้คำสร้าง print ใน input
    sum += num

print(sum)
print("ค่าเฉลี่ย =",sum/4)