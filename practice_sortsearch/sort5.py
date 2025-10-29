class Team:
    def __init__(self,name,wins,loss,draws,scored,conceded):
        self.name = name
        self.wins = int(wins)
        self.loss = int(loss)
        self.draws = int(draws)
        self.scored = int(scored)
        self.conceded = int(conceded)
        self.point = self.wins * 3 + self.draws * 1
        self.gd = self.scored - self.conceded
    
    def __str__(self):
        return (str([self.name,{'points':self.point},{'gd':self.gd}]))

def sort(teams):
    for last in range(len(teams)-1,0,-1):
        swap = False
        for i in range(last):
            if teams[i].point < teams[i+1].point:
                teams[i],teams[i+1] = teams[i+1],teams[i]
                swap = True
            elif teams[i].point == teams[i+1].point:
                if teams[i].gd < teams[i+1].gd:
                    teams[i],teams[i+1] = teams[i+1],teams[i]
                    swap = True
            
        if not swap:
            break
    
teams = []
team = input("Enter Input : ").split('/')
for t in team:
    name,win,loss,draw,scored,connected = t.split(',')
    teams.append((Team(name,win,loss,draw,scored,connected)))
print('== results ==')
sort(teams)
for t in teams:
    print(t)