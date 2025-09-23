def insertion(l):
    for i in range(1,len(l)):
        iEle = l[i]
        for j in range(i,-1,-1):
            if j > 0 and l[j-1] > iEle:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break

def sorting(card,mode):
    order_num = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,
                 'T':8,'J':9,'Q':10,'K':11,'A':12}
    order_symbol = {'C':0,'D':1,'H':2,'S':3}
    found = []
    cards = []
    for c in card:
        

        if c[0] not in order_symbol or len(c) >2:
            print(f"Error: {c} is an invalid card")
            continue
        if c in found :
            print(f"Error: Duplicate card found - {c}")
            continue
        cards.append(c)
        found.append(c)
    
    if len(cards) == 0:
        print("No valid cards to sort.")
        return 
    def compare(a, b):
        sa, na = a[0], a[1:]
        sb, nb = b[0], b[1:]
        if mode == "num":
            if order_num[na] != order_num[nb]:
                return order_num[na] - order_num[nb]
            return order_symbol[sa] - order_symbol[sb]
        elif mode == "symbol":
            if order_symbol[sa] != order_symbol[sb]:
                return order_symbol[sa] - order_symbol[sb]
            return order_num[na] - order_num[nb]
        return 0
    
    
    for i in range(1,len(cards)):
        key = cards[i]
        j = i -1
        while j >= 0  and compare(cards[j],key) >0 :
            cards[j+1] = cards[j]
            j -= 1
        cards[j+1] = key
    
    

    print(f"Sorted cards : {' '.join(str(card) for card in cards)} ")

print("Have fun with sort card")
card,mode = input("Enter Input: ").split('/')
card = list(card.split(','))
if mode == '':
    print("No valid cards to sort.")
else:
    sorting(card,mode)
