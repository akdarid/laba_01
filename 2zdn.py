a = (input("a: "))
b = (input("b: "))
while "," in a or "," in b:
    a = a.replace(",", ".")
    b = b.replace(",", ".")
print(f'sum={float(a) + float(b)}; avg = {(float(a) + float(b)) / 2}')