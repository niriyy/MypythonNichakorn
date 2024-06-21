b=int(input("จำนวนเลขที่บวก:"))
for n in range(b):
    t=int(input("เลขที่ต้องการบวก %d."%(n+1)))
    b=b+t
    
print(f"ผลรวม {b} ")
