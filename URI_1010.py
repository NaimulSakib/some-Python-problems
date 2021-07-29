
code1,unit1,price1=input().split()
code2,unit2,price2=input().split()
code1=int(code1)
unit1=int(unit1)
price1=float(price1)                          # Uri 1010........
code2=int(code2)
unit2=int(unit2)
price2=float(price2)
value=price1*unit1+unit2*price2
print("VALOR A PAGAR: R$ %.2f"%value)
