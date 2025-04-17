password = input("Parol daxil edin: ")

if len(password) < 8:
    print("Parol ən az 8 simvol olmalıdır.")
elif " " in password:
    print("Parolda boşluq olmamalıdır.")
elif not any(ch.isupper() for ch in password):
    print("Parolda ən az 1 böyük hərf olmalıdır.")
elif not any(ch.islower() for ch in password):
    print("Parolda ən az 1 kiçik hərf olmalıdır.")
elif not any(ch.isdigit() for ch in password):
    print("Parolda ən az 1 rəqəm olmalıdır.")
else:
    print("Təhlükəsiz parol ✅")
