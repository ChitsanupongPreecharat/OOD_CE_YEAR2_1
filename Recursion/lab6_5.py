def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n-1)+fib(n-2)

def find(purity, weight):
    if purity == 1:
        return weight

    c_k = fib(purity - 1)
    
    total_weight_prev_level = 2 * weight - c_k + 1
    
    if total_weight_prev_level < 2:
        return -1
        
    
    weight_a = total_weight_prev_level // 2
    weight_b = total_weight_prev_level - weight_a
    
    result_a = find(purity - 1, weight_a)
    result_b = find(purity - 1, weight_b)

    if result_a == -1 or result_b == -1:
        return -1
        
    return result_a + result_b


n, w = map(int, input("Purity and Weight needed: ").split())
print(f"Total weight of used minerals with Purity 1 : {find(n,w)}")
