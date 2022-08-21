import random
from typing import Dict, List, Optional, Iterable

class Card(object):
  values: Dict[str, int] = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "A": 11
    
  }
  suits = ("Diamonds", "Clubs", "Heart", "Spades")
  
  ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "A")
  
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = self.values[rank]
    
  def __str__(self):
    return self.rank + " of " + self.suit



class Deck(Card):
  def __init__(self):
    self.all_cards = []
    for suit in Card.suits:
      for rank in Card.ranks:
        self.all_cards.append(Card(suit, rank))
        
  def shuffle(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()


# each player and dealer will have their own hand just like me
class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def adjust_for_ace(self):
    if self.value > 21 and self.aces > 0:
      self.value -= 10
      self.aces -= 1
  
  def add_card(self, card):
    self.cards.append(card)
    self.value += card.value
    if card.rank == 'A':
      self.aces += 1
      
    self.adjust_for_ace()
  
# general functions

def hit(deck, hand):
  hand.add_card(deck.deal_one())


def hit_or_stand(deck,hand):
  global playing
  result = input("Hit (yes/no/showcard)? ")
  if result.lower() == 'yes':
    hit(deck,hand)
  elif result.lower() == 'no':
    playing = False
  elif result.lower() == "showcard":
    for card in hand.cards:
      print(card)

# set up game conditions

def player_busts(player, dealer):
  if player.value > 21:
    # prints hand
    print("Player busts, dealer wins")

def player_wins(player, dealer):
  if player.value > dealer.value and player.value <= 21:
    # print hand
    print("Player wins!")

def dealer_busts(player, dealer):
  if dealer.value > 21:
    # prints hand
    print("Dealer busts, player wins")
    

def dealer_wins(player, dealer):
  if dealer.value > player.value and dealer.value <= 21:
    # print hand
    print("Dealer wins!")
    


# game loop
while True:
  print("Welcome to BlackJack aka 21")

  #create deck and deal out cards
  deck = Deck()
  deck.shuffle()
  p_Hand = Hand()
  d_Hand = Hand()

  # deal two cards to player and dealer
  p_Hand.add_card(deck.deal_one())
  p_Hand.add_card(deck.deal_one())
  d_Hand.add_card(deck.deal_one())
  d_Hand.add_card(deck.deal_one())
  
  global playing
  playing = True
  while playing:
    hit_or_stand(deck, p_Hand)
    # different game conditions
    if p_Hand.value > 21:
      player_busts(p_Hand, d_Hand)
      break
  if p_Hand.value <= 21:
    while d_Hand.value <= 21:
      hit(deck, d_Hand)
    
    player_wins(p_Hand,d_Hand)
    dealer_busts(p_Hand,d_Hand)
    dealer_wins(p_Hand,d_Hand)
    # PRINT DEALER Hand
  for card in d_Hand.cards:
    print(card)
      
  if input("Play again (y/n)? ").lower() != 'y':
    break
  else:
    playing = True




