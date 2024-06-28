#bmi
def cal(kg,cm):
    bmi = kg/((cm/100)**2)
    
    return bmi

def tt(bmi):
    print("ค่าดัสนี = ",bmi)
    if bmi<18.50:
        print("น้ำหนักน้อย/ผอม")
    
    elif bmi<=18.50 and bmi>=22.90:
        print("ปกติ(สุขภาพดี)")
    elif bmi<=23 and bmi>=24.90:
        print("ท้วม/โรคอ้วนระดับ1")
    elif bmi<=25 and bmi>=29.90:
        print("ท้วม/โรคอ้วนระดับ2")

    else:
        print("อ้วม/โรคอ้วนระดับ3")
        
tt(cal(45,140))