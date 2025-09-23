# หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล

# เช่น

# hbd(65) = "saimai is just 21, in base 32!"

# hdb(21) = "saimai is just 21, in base 10!"

# hdb(8888) = "saimai is just 20, in base 4444!"

def hbd(age):
    for value in [20, 21]:
        digit_1 = value // 10
        digit_0 = value % 10
        
        base = (age - digit_0) / digit_1
        
        if base.is_integer() and base > digit_1 and base > digit_0:
            return f"saimai is just {value}, in base {int(base)}!"
    

year = int(input("Enter year : "))
print(hbd(year))
