n = int(input("How many numbers? "))

for i in range(0, n):
    words = input("Now type case " + str(i) + ": ").split(' ')
    print("Case #%d:" % (i))
    for i in words[::-1]:
        print(i, " ", end='')
    print()