



book_shop , book_want = input("Enter input: ").split('/')
book_shop = list(book_shop.split())
book_want = list(book_want.split())
money = 0
not_found = []
for b in book_want:
    if b in book_shop:
        index = book_shop.index(b) 
        book_shop.pop(index)
        book_shop.insert(0,b)
        money += index+1
        print(f'Search {b} -> found at {index+1} move to front ->  {(' '.join(book_shop))}')
    else:
        if b not in not_found:
            money += len(book_shop)+1
            not_found.append(b)
            print(f'Search {b} -> not found -> {(' '.join(book_shop))}')
        else:
            money += 1
            book_shop.insert(0,b)
            not_found.remove(b)
            print(f'Search {b} -> add new book ->  {(' '.join(book_shop))}')


print()
print(f'Final books: {(' '.join(book_shop))}')
print(f'Total cost: {money}')