def binary_search(arr, target):
    """
    Standard iterative binary search.
    Note: Requires the array to be sorted to work correctly.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def solve():
    print("This is your BOOK!!!")
    
    # Input Processing
    raw_input = input("Enter input: ")
    if '/' not in raw_input:
        return
        
    books_part, search_part = raw_input.split('/')
    books = books_part.split()
    target_books = search_part.split()
    
    total_cost = 0
    not_found_tracker = set()

    for target in target_books:
        # We use a linear search here because the 'Move to Front' 
        # rule keeps the list unsorted, making binary_search unusable.
        if target in books:
            idx = books.index(target)
            total_cost += (idx + 1)
            
            # Move to Front logic
            books.pop(idx)
            books.insert(0, target)
            print(f"Search {target} -> found at {idx + 1} move to front -> {' '.join(books)}")
            
        else:
            if target not in not_found_tracker:
                total_cost += (len(books) + 1)
                not_found_tracker.add(target)
                print(f"Search {target} -> not found -> {' '.join(books)}")
            else:
                total_cost += 1
                not_found_tracker.remove(target)
                books.insert(0, target)
                print(f"Search {target} -> add new book -> {' '.join(books)}")

    print(f"\nFinal books: {' '.join(books)}")
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    solve()
