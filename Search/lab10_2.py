print("This is your BOOK!!!")
def binary_search(books,target):
    left = 0
    right = len(books) - 1
    while left <= right:
        mid = (left + right) // 2
        if books[mid] is target:
            return mid
        if books[mid] < target:
            left = mid+1
        else:
            right= mid-1
    return -1





books,want_books = input("Enter input: ").split('/')
books = books.split()
want_books = want_books.split()
money = 0

not_found = []
for b in want_books:
    
    if b in books:
        index = books.index(b)
    else:
        index = -1
    if index != -1:
        money += index +1
        books.pop(index)
        books.insert(0,b)
        print(f"Search {b} -> found at {index+1} move to front ->  {' '.join(books)}")
    else:
        if b not in not_found:
            money += len(books) + 1
            not_found.append(b)
            print(f"Search {b} -> not found -> {' '.join(books)}")
        else:
            money += 1
            not_found.remove(b)
            books.insert(0,b)
            print(f"Search {b} -> add new book ->  {' '.join(books)}")

print()
print(f"Final books: {' '.join(books)}")
print(f"Total cost: {str(money)}")