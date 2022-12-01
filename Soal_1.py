print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
a = int(input("Enter choice(1/2/3/4): "))
def hitung_angka():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

if a == 1:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    add = (x+y)
    print(x, "+", y,"=",add)
elif a == 2:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    subtract = (x-y)
    print(x, "-",y,"=",subtract)
elif a == 3:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    multiply = (x*y)
    print(x,"*",y, "=",multiply)
elif a == 4:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    divide = (x/y)
    print(x, "/",y, "=", divide)
hitung_angka()
