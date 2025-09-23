class Queue:
    def __init__(self):
        self.item = []
    def enQueue(self,i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def is_Empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)                

print(" ***Cafe***")
custumers = list(input("Log : ").split('/'))
q = Queue()
for i,c in enumerate(custumers):
    si,pi = map(int,c.split(','))
    q.enQueue({'id':i+1, 'arrive':si, 'make_time':pi})

barista = [0,0]
result = []
max_wait = 0
max_with_id = None

while not q.is_Empty():
    cus = q.deQueue()
    c_id = cus['id']
    arrive = cus['arrive']
    make_time = cus['make_time']

    soonest_idx = 0 if barista[0] <= barista[1] else 1
    start = max(arrive, barista[soonest_idx])
    end = start + make_time
    barista[soonest_idx] = end

    wait_time = start - arrive
    if wait_time > max_wait:
        max_wait = wait_time
        max_with_id = c_id

    result.append({'time':end,'cus':c_id})
    

for r in sorted(result,key=lambda x:x['time']):
    print(f"Time {r['time']} customer {r['cus']} get coffee") 
if max_wait == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {max_with_id}")
    print(f"The customer waited for {max_wait} minutes")
