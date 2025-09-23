def sort_l(l):
    if l == []: return []
    else:
        m = max(l)
        l.remove(m)
        return [m] + sort_l(l)
        
       

l = list(map(int,input("Enter your List : ").split(',')))

print(f"List after Sorted : {sort_l(l)}")
