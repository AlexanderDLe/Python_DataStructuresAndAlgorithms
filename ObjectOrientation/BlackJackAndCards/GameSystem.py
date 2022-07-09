import os, sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from Deck import Deck, Hand
from Account import Player
############################

class GameRound:
  def __init__(self, potValue):
    pass

class Bet:
  def __init__(self, player, chips):
    self.chips = chips

class GameSystem:
  def __init__(self, players):
    self.deck: Deck = Deck()
    self.players = players
    self.bets = []
    self.currentPot = 0
  
  def beginRound(self):
    self.placeBets()
    
  def distributeCards(self):
    for player in self.players:
      card1 = self.deck.pop()
      card2 = self.deck.pop()      
      hand = Hand([card1, card2])

      player.obtainHand(hand)
    
  def hit(self, player: Player):
    playerHand: Hand = player.getHand()
    if playerHand.isValid() == False: return
    playerHand.takeCard(self.deck.pop())
    
    
  def placeBet(self, player, chips): 
    bet = Bet(player, chips)
    self.bets.append(bet)
  


def runSolution():
  player1 = Player('name', 'email')
  player2 = Player('name', 'email')
  player3 = Player('name', 'email')
  players = [player1, player2, player3]
  
  game = GameSystem(players)
  game.beginRound()
runSolution()