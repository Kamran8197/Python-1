course = {
    "name": "Full-Stack Python",
    "muddet": 6,
    "movzu": ["Python", "SQL", "API", "Docker"]
}

course["movzu"].append("React")
course["muddet"] += 1

if "API" in course["movzu"]:
    print("API mövzusu öyrəniləcək")

print(course)
