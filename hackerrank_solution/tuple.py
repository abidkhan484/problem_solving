if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    li = []
    for i in range(n):
        li.append(i)

    t=tuple(li)
    del li

    print(hash(t))

    
