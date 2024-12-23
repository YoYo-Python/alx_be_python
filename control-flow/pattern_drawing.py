pattern_size = int(input("Enter the size of the pattern:"))
counter = 0
while counter < pattern_size:
    for i in range(pattern_size):
        print("*", end="")
    print()
    counter = counter + 1
