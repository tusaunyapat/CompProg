import random
# แสดงภาพไพ่
def random_card(n):
  # ค่าไพ่ A, 2, 3, 4, 5, 6, 7, 8, 9, T (ใช้แทน 10), J, Q,และ K
  # ชุดไพ่ C (แทน Clubs), D (แทน Diamonds ), H (แทน Hearts), และ S (แทน Spades)
  # สมมติให้ไพ่ซ้ำกันได้
  suits = "CDHS"
  ranks = "A23456789TJQK"
  cards = []
  for _ in range(n):
    n_r = random.randrange(len(ranks))  
    n_s = random.randrange(len(suits))  
    c = suits[n_s] + ranks[n_r]
    cards.append(c)
    
  return cards


def print_card(n):
  cards = random_card(n)
  cards.sort()
  print(cards)
  


n = int(input())
print_card(n)