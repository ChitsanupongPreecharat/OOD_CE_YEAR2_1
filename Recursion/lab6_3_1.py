result = []
def Combination(input_list, answer=[]):
    if not input_list:
        if answer: 
            result.append(answer)
        return

    
    Combination(input_list[1:], answer + [input_list[0]])

    
    Combination(input_list[1:], answer)

num = list(map(int, input("Enter Input: ").split()))
Combination(num)
print(f"Output: {result}")