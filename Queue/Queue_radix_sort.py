from collections import deque
import time 
class Queue:
    def __init__(self):
        self.item = deque()
    def enQueue(self,i):
        self.item.append(i)
    def deQueue(self):
        return self.item.popleft()
    def is_Empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item) 



def radix_sort(numbers):
    
    def get_max_digits(numbers):
        return len(str(max(numbers)))
    def get_digits_at_position(number,position):
        return (number//(10**position)) % 10
    
    max_digits = get_max_digits(numbers)
    digit_queue = [Queue() for _ in range(10)]

    for position in range(max_digits):
        for number in numbers:
            digit = get_digits_at_position(number,position)
            digit_queue[digit].enQueue(number)
        numbers = []
        for queue in digit_queue:
            while not queue.is_Empty():
                numbers.append(queue.deQueue())
    return numbers            
start = time.time()
numbers = list(map(int,input("input : ").split()))
print(radix_sort(numbers))
stop = time.time()
print("time: ",stop-start)