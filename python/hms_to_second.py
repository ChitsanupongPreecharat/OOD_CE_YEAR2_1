h,m,s = map(int,input("Enter HH MM SS : ").split())

if h <0 or h >=60 :
    print(f'hh({h}) invalid')

elif m <0 or m >=60 :
    print(f'mm({m}) invalid')

elif s <0 or s >=60 :
    print(f'ss({s}) invalid')
else:
    print(f"{h}:{m}:{s} = {(h*3600) + (m*60) + s} seconds")    