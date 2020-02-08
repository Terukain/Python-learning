import random
type1 = ["♥","♠","♦","♣"]
number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def productcard():
    cards=[]
    for i in type1:
        for j in number:
            cards.append(i+j)
    cards.append(("joker","red"))
    cards.append(("Joker","black"))
    return cards
cards=productcard()
random.shuffle(cards)
player1Cards = []
player2Cards = []
player3Cards = []
covercards=3
for k in range(0,len(cards)-covercards):
    card=cards[k]
    if k % 3==0:
        player1Cards.append(card)
    if k % 3==1:
        player2Cards.append(card)
    if k % 3==2:
        player3Cards.append(card)
dipai= cards[-3:] 
print("玩家1：\n",player1Cards)
print("玩家2：\n",player2Cards)
print("玩家3：\n",player3Cards)
print("底牌:\n",dipai)

