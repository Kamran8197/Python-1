numbers = []
for i in range(5):
    num = int(input(f"{i+1}-ci ədədi daxil edin: "))
    numbers.append(num)

unique_sum = sum(set(numbers))
print("Fərqli ədədlərin cəmi:", unique_sum)
