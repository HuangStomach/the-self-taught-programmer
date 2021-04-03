nums = [4, 36, 10, 12, 48]

while True:
    i = input("Plz input a num, q to quit:\n")
    if i == 'q':
        break
    for num in nums:
        if int(i) == num:
            print("yes")
            break
