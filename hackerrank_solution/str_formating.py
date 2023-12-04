def print_formatted(number):
    p = len(str(number))
    q = len(oct(number))-2
    r = len(hex(number))-2
    s = len(bin(number))-2
    for i in range(1, number+1):
        print(str(i).rjust(p), oct(i)[2:].rjust(q), hex(i)[2:].upper().rjust(r), bin(i)[2:].rjust(s))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
