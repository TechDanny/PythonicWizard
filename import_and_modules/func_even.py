def add_even():
    total = 0
    numbers = []
    n = int(input("List size: "))
    for i in range(0, n):
        nums = int(input(f"Insert your numbers {i + 1}: "))
        numbers.append(nums)
        if nums % 2 == 0:
            total += nums
    return total
