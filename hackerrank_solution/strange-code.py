# i think this time, it's solved

n = int(input().strip())
counter = 3; i = 1
while True:
    if n < i:
        print(i - n )
        break
    i += counter
    counter += counter

