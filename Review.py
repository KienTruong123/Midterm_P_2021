"""
Author: Truong Dinh Kien
Date Created: March 21, 2021
"""

# Midterm review
import random
import itertools

#1 a Both dice are the same
def P_dice1(n):
    count=0
    for i in range(n):
        if random.randint(1,6)==random.randint(1,6):
            count+=1
    return count/n
#b Both dice are different
def P_dice2(n):
    return 1-P_dice1(n)

#c Both dice are even
def P_dice3(n):
    count=0
    for i in range(n):
        if random.randint(1,6)%2==random.randint(1,6)%2==0:
            count+=1
    return count/n
#d Both dice are odd
def P_dice4(n):
    count=0
    for i in range(n):
        if random.randint(1,6)%2==random.randint(1,6)%2==1:
            count+=1
    return count/n
#e One die is even and the other is odd
def P_dice5(n):
    count=0
    for i in range(n):
        if (random.randint(1,6)+random.randint(1,6))%2==1:
            count+=1
    return count/n
#f Both dice are 6
def P_dice6(n):
    count=0
    for i in range(n):
        if random.randint(1,6)==random.randint(1,6)==6:
            count+=1
    return count/n
#g Summation of both dice are greater than 10.
def P_dice7(n):
    count=0
    for i in range(n):
        if (random.randint(1,6)+random.randint(1,6))>10:
            count+=1
    return count/n

#2 a All 3 balls are same color.
cross = lambda A,B: {a+b for a in A for b in B}
urn= cross('b','12')|cross('r','123')|cross('w','12345')
def draw1(n):
    count=0
    for i in range(n):
        d=random.sample(urn,3)
        if(d[0][0]==d[1][0]==d[2][0]):
            count+=1
    return count/n
#b All 3 balls are different colors.
def draw2(n):
    count=0
    for i in range(n):
        d=random.sample(urn,3)
        if(d[0][0]!=d[1][0]!=d[2][0]!=d[0][0]):
            count+=1
    return count/n

#c Only 2 balls are same color.
def draw3(n):
    count=0
    for i in range(n):
        d=random.sample(urn,3)
        if(d[0][0]!=d[1][0]==d[2][0] or d[0][0]==d[1][0]!=d[2][0] or d[0][0]==d[2][0]!=d[1][0]):
            count+=1
    return count/n

#d There are 2 red balls and 1 white ball.
def draw4(n):
    count=0
    for i in range(n):
        d=random.sample(urn,3)
        if (d[0][0]=='w' and d[1][0]== d[2][0]=='r') or (d[0][0]==d[1][0]\
            =='r'and d[2][0]=='w') or (d[0][0]==d[2][0]=='r' and d[1][0]=='w'):
            count+=1
    return count/n
#e List all the cases that all 3 balls are white. (return probability and list)
def draw5(n):
    result=[]
    for i in range(n):
        d=random.sample(urn,3)
        if(d[0][0]==d[1][0]==d[2][0]=='w'):
            result.append(d)
    return (len(result)/n,result)

#3 a All 4 cards are from the same suit.
pos='23456789TJKQA'
cards=cross('D',pos)|cross('H',pos)|cross('C',pos)|cross('S',pos)
def poker1(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        if(d[0][0]==d[1][0]==d[2][0]==d[3][0]):
            count+=1
    return count/n
#b All 4 cards are differents suits.
def poker2(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        if d[0][0]!=d[1][0]!=d[2][0]!=d[3][0]!=d[0][0]!=d[2][0] and d[1][0]!=d[3][0]:
            count+=1
    return count/n
#c All 4 cards are same color.
def poker3(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        temp=0
        for k in d:
            if k[0] in ['D','H']:
                temp+=1
        if temp==4 or temp==0:
            count+=1
    return count/n
#d All 4 cards are same value.
def poker4(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        if(d[0][1]==d[1][1]==d[2][1]==d[3][1]):
            count+=1
    return count/n
#e All 4 cards are numbers.
def poker5(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        temp=0
        for k in i:
            if k[1] in '23456789T':
                temp+=1
        if temp==4:
            count+=1
    return count/n
#f All 4 cards are faces.
def poker6(n):
    count=0
    for i in range(n):
        d=random.sample(cards,4)
        temp=0
        for k in i:
            if k[1] in '23456789T':
                temp+=1
        if temp==0:
            count+=1
    return count/n
#4
URN= cross('w','12')|cross('b','123')|cross('r','1234')
U3=list(itertools.permutations(URN,3))
white1blue1red1=[]
for i in U3:
    if i[0][0]!=i[1][0]!=i[2][0]!=i[0][0]:
        white1blue1red1.append(i)
P=len(white1blue1red1)/len(U3)   
#5 a Theorical probability
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
Suits = {'D', 'H', 'C', 'S'}
U = list(itertools.combinations(list(itertools.product(Ranks , Suits)),5))
def P_A(U):
    straights = 0
    for straight in U:
        if straight[0][1]== straight[1][1]==straight[2][1]==straight[3][1]==straight[4][1]:
            continue # excluding royal flush and straight flush
        values = [ card[0] for card in straight]
        if  (max(values) - min(values) == 4 and len(set(values))==5) or {1,10,11,12,13}==set(values):
            straights+=1
    return straights/len(U)

#b Practical probability
def P_B(U,n):
    count=0
    max_index=len(U)-1
    for i in range(n):
        t=U[random.randint(0,max_index)]
        if t[0][1]== t[1][1]==t[2][1]==t[3][1]==t[4][1]:
            continue # excluding royal flush and straight flush
        values = [ card[0] for card in t]
        if  (max(values) - min(values) == 4 and len(set(values))==5) or {1,10,11,12,13}==set(values):
            count+=1
    return count/n

#6a 
E = {0,1,2,3,4,5}
E1=[]
E2=[]
for i in list(itertools.product(E,repeat=3)):
    if i[0]!=0:
        E1.append(i[0]*100+i[1]*10+i[2])
#b 
for i in itertools.permutations(E,4):
    if i[0]!=0:
        E2.append(i[0]*1000+i[1]*100+i[2]*10+i[3])

