def Combination(input_list, answer = []):
    if not input_list:
        if answer:
            result.append(answer)
        return 
    Combination(input_list[1:],answer+[input_list[0]])
    Combination(input_list[1:],answer)


result = []

Input = list(map(int,input("Enter Input: ").split()))
Combination(Input)
print(result)