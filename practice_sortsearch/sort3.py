def sort(card,method):
    order_num = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
    order_symbol = {'C':0,'D':1,'H':2,'S':3}


    cards = []
    for c in card:
        if c[0] not in order_symbol or len(c) > 2:
            print(f"Error: {c} is an invalid card")
            continue
        if c in cards:
            print(f"Error: Duplicate card found - {c}")
            continue
        cards.append(c)

    if len(cards) == 0:
        print("No valid cards to sort.")
        return
    
    def compare(a,b):
        sa , na = a[0] , a[1] 
        sb , nb = b[0] , b[1] 
        if method == 'num':
            if order_num[na] != order_num[nb]:
                return int(order_num[na] - order_num[nb])
            return order_symbol[sa] - order_symbol[sb]
        elif method == 'symbol':
            if order_symbol[sa] != order_symbol[sb]:
                return int(order_symbol[sa] - order_symbol[sb])
            return order_num[na] - order_num[nb]
        return 0
    
    for i in range(1,len(cards)):
        key = cards[i]
        j = i-1
        
        while j >= 0 and compare(cards[j],key) > 0:
            cards[j+1] = cards[j]
            j -= 1
        cards[j+1] = key
            
            


                
    print(f"Sorted cards : {' '.join(str(c) for c in cards)}")



card,method = input("Enter Input: ").split('/')
card = list(card.split(','))
sort(card,method)
