import random

secret = random.randint(1, 10)
for attempt in range(1, 4):
    guess = int(input(f"{attempt}. təxmininizi edin (1–10): "))
    if guess == secret:
        print("Təbriklər! Tapdınız ✅")
        break
    elif guess < secret:
        print("Daha böyük ədəd seçin.")
    else:
        print("Daha kiçik ədəd seçin.")
else:
    print(f"Təəssüf! Gizli ədəd {secret} idi.")
