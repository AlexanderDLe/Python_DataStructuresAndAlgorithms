from enum import Enum
from random import shuffle

class Suit(Enum):
  Heart = 1
  Spade = 2
  Diamond = 3
  Club = 4

class HandStatus(Enum):
  Valid = 1
  Invalid = 2

class Card:
  def __init__(self, suit, faceValue):
    self.faceValue = faceValue
    self.suit = suit

class BlackJackCard(Card):
  def __init__(self, suit, faceValue):
    super().__init__(suit, faceValue)
    self.gameValue = faceValue if faceValue < 10 else 10
  
  def __repr__(self):
    return f'|{self.gameValue}|'
  
  def getGameValue(self):
    return self.gameValue
    
class Deck:
  def __init__(self):
    self.cards = []
    self.reset()
    
  def initDeck(self):
    self.cards = []
    
    for i in range(1, 14):
      self.cards.append(BlackJackCard(Suit.Heart, i))
      self.cards.append(BlackJackCard(Suit.Club, i))
      self.cards.append(BlackJackCard(Suit.Diamond, i))
      self.cards.append(BlackJackCard(Suit.Spade, i))
      
  def shuffleDeck(self):
    shuffle(self.cards)
    
  def reset(self):
    self.initDeck()
    self.shuffleDeck()
    
  def pop(self):
    return self.cards.pop()
        
class Hand:
  def __init__(self, cards, status = HandStatus.Valid):
    self.cardSum = 0
    self.cards = cards
    self.status = status
    
  def takeCard(self, card: BlackJackCard):
    self.cards.append(card)
    self.cardSum += card.getGameValue()
    
    if self.cardSum > 21:
      self.status = HandStatus.Invalid
      
  def isValid(self):
    return self.status == HandStatus.Valid
  
  def getCardSum(self):
    return self.cardSum
