def beforeMidterm(a,b,c):
    score = a+b+c
    return score

while(True):
    a = int(input("รับค่าคะแนนเก็บ: "))
    if(a>20):
        print("กรอบค่าใหม่")
    else:
        print("ยืนยันค่า")
        break

while(True):
    b = int(input("รับค่าคะแนนจิตพิสัย: "))
    if(b>10):
        print("กรอบค่าใหม่")
    else:
        print("ยืนยันค่า")
        break
        
while(True):
    c = int(input("รับค่าคะแนนกลางภาค: "))
    if(c>20):
        print("กรอบค่าใหม่")
    else:
        print("ยืนยันค่า")
        break

print("คะแนนก่อนกลางภาค: %d" % beforeMidterm(a,b,c))