from enum import Enum

class Cell:
  def __init__(self, piece, x, y):
    self.piece = piece
    self.x = x
    self.y = y
  
  def getPiece(self): pass
  def setPiece(self): pass
  
class Allegiance:
  Black: 1
  White: 2
  
class Piece:
  def __init__(self, allegiance): pass
  def move(self): pass
  def setAllegiance(self): pass
  def setKilled(self): pass
  def getKilled(self): pass
  def canMove(): pass
  
class King(Piece):
  def __init__(self, allegiance):
    super().__init__(allegiance)
  def canMove(): pass
  
class Board:
  def __init__(self):
    pass
  def getBox(self, x, y): pass
  def resetBoard(self): pass
  
class Player:
  def __init__(self, allegiance): pass
  def isWhite():pass

class Move:
  def __init__(self, player, startBox, endBox, pieceKilled): pass
  def isCastling(): pass

class Game:
  def __init__(self):
    self.players = []
    self.board = Board()
    self.currentTurn = None
    self.status = ''
    self.movesPlayed = []
    
  def startGame(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.board.resetBoard()
    
    if player1.isWhite():
      self.currentTurn = player1
    else:
      self.currentTurn = player2
  
    self.movesPlayed = []

  def playerMove(self, player, start, end): pass
  def makeMove(self): pass
  