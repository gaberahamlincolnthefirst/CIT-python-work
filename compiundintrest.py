PV = float(input("Enter the starting principal: "))
R = float(input("Enter the anualinterest rate: "))
m = float(input ("How many times per year is the interest compounded? : "))
t = int(input("For how many years will the account earn interest? : "))
r = float(R / 100)
FV = PV * (1 + r/m)**(t*m)
print(" At the end of", t,"years you will have $ ", FV )

