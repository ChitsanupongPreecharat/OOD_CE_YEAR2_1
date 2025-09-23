def fib(n):
    if n == 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

def fine(purity,weight):
    if purity == 1:
        return weight
    
    ck = fib(purity-1)
    prev_weight = 2 * weight -ck + 1
    
    if prev_weight <2:
        return -1
    
    weight_a = prev_weight // 2
    weight_b = prev_weight - weight_a

    result_a = fine(purity-1,weight_a)
    result_b = fine (purity-1,weight_b)

    if result_a == -1 or result_b == -1:
        return -1

    return result_a+result_b

purity,weight = map(int,input("Purity and Weight needed: ").split())
print(fine(purity,weight))
