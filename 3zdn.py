price = int(input())
discount = int(input())
vat = int(input())
print(f"База после скидки: {price * (1 - discount/100)}0")
print(f'НДС:               {(price * (1 - discount/100)) * (vat/100)}0')
print(f'Итого к оплате     {(price * (1 - discount/100)) + (price * (1 - discount/100)) * (vat/100)}0')

