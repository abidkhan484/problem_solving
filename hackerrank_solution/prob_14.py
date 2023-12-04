class Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
        check = 0
        self.maximumDifference = -1000
        length = len(self.__elements)

        for i in range(length):
            for j in range (i+1, length):
                check = a[i] - a[j]
                
                
                if check < 0:
                    check = -check

                if check > self.maximumDifference:
                    self.maximumDifference = check

        return self.maximumDifference



# End of Difference class

__ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
