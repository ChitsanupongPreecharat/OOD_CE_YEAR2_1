def sort(animal, method):
    def compare(a, b):
        if method == 'W':
            return sum(ord(i) - 96 for i in a) - sum(ord(j) - 96 for j in b)
        
        elif method == 'V':
            priority = {'a': 5, 'e': 4, 'i': 3, 'o': 2, 'u': 1}
            count_a = sum(ch in priority for ch in a)
            count_b = sum(ch in priority for ch in b)
            if count_a != count_b:
                return count_a - count_b
            max_a = max((priority[ch] for ch in a if ch in priority), default=0)
            max_b = max((priority[ch] for ch in b if ch in priority), default=0)
            return max_b - max_a

    for last in range(len(animal) - 1, 0, -1):
        swap = False
        for i in range(last):
            if compare(animal[i], animal[i + 1]) > 0:  
                animal[i], animal[i + 1] = animal[i + 1], animal[i]
                swap = True
        if not swap:
            break

    print(' '.join(animal))


animal, method = input("Enter Input : ").split('/')
animal = animal.split()
sort(animal, method)
