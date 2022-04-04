"""
เรื่อง for-while การวนลูปหรือทำซ้ำ
"""
# เข้าสู้การเขียนโค้ด (ไม่ใช่เเบบบฝึกหัด)

from re import I


x = range(10) #0-9
Y = range(1,10) #1-9
E = range(100,200) #100-199

for i in E:
    print(i)



"""
การตรวจสอบว่าเป็นคำสั่งของ start , stop , step
"""

start = x.start
stop = x.stop

start1 = Y.start
stop1 = Y.stop

start2 = E.start
stop2 = E.stop

print(start,stop)
print(start1,stop1)
print(start2,stop2)