score=int(input("รับค่าคะแนน : "))

if score >= 0 and score <= 100:
    if score >= 80 and score <= 100:
        print("เกรดA")
    elif score >= 70 and score <= 79:
        print("เกรดB")
    elif score >= 60 and score <= 69:
        print("เกรดC")
    elif score >= 50 and score <= 59:
        print("เกรดD")
    elif score >= 0 and score <= 49:
        print("เกรดF")
else:
    print("กรุณากรอกข้อมูล0-100")
 
