def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

#print(is_odd(17))
#print(is_even(23))



#simple recursion
#this function go to the end and sum the previous to the start

def listsum(ls):
    #Base condition
    if not ls:
        return 0

    #first element + result of calling 'listsum' with rest of the element
    return ls[0]+listsum(l[1:])



#Tail call recursion
#this function sum from the first till the end

def listsum_tail(ls, result):
    #Base condition
    if not ls:
        return result

    #sum from the first element of the list
    return listsum_tail(ls[1:], result + ls[0])



#passing around index version

def listsum_index(ls, index, result):
    #Base condition
    if index==len(ls):
        return result

    #call with next index and add the current element to result
    return listsum_index(ls, index+1, result+ls[index])


#inner function version
#we just make a function on the function for the result value

def listsum_inner(ls):
    def recursion(index, result):
        #Base condition
        if not ls:
            return result

        return recursion(index+1, result+ls[index])

    return recursion(0, 0)


#default parameter version

def listsum_default(ls, index=0, result=0):
    if not ls:
        return result

    return listsum_default(ls, index+1, result+ls[index])


#reverse a list

def reverse_list(li, l=0):
    le = len(li)
    if not (l<(le//2)):
        return li
    temp = li[l]
    li[l] = li[le-(l+1)]
    li[le-(l+1)] = temp
    return reverse_list(li, l+1)

print(reverse_list([1,2,3,4]))
print(reverse_list([1,2,3,4,5]))
