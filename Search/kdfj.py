def fine_near_prime(n):
            n = n*2
            i = 2
            while n % i == 0:
                n +=1
            return n

print(fine_near_prime(9))