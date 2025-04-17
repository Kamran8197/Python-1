a = float(input("Birinci ədədi daxil edin: "))
b = float(input("İkinci ədədi daxil edin: "))
operation   = input("Əməliyyatı seçin (+, -, *, /): ")

if operation == "+":
    print(f"Nəticə: {a + b}")
elif operation == "-":
    print(f"Nəticə: {a - b}")
elif operation == "*":
    print(f"Nəticə: {a * b}")
elif operation == "/":
    if b == 0:
        print("Xəta: 0-a bölmə mümkün deyil!")
    else:
        print(f"Nəticə: {a / b}")
else:
    print("Əməliyyat tanınmadı!")
