def FF(c):
    F = (9/5)*c+32
    return F

def KK(c):
    K = c+273.15
    return K

c = float(input("รับค่าองศาเซลเซียส :"))
print("องศาฟาเรนไฮส์ : %.2f" % FF(c))
print("องศาเคลวิน : %.2f" % KK(c))
