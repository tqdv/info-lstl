# Returns a list of n primes
def e(n):
    if n < 1 :
        return []
    
    list = [2]
    if n == 1 :
        return list
    
    count = 1
    num = 3
    while count < n :
        length = len(list)
        isPrime = True
        index = 0
        while isPrime == True and index < length :
            if num % list[index] == 0 :
                isPrime = False
            index += 1
        if isPrime :
            list.append(num)
            count += 1
        num += 2
    return list

#print(e(5))
#print(e(25))
