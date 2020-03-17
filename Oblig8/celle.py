class Celle:

  def __init__(self):
      """ The default status of the cell is; dead """
      self._status = False

  # Change status
  def settDoed(self):
      """ Set the cell staus to dead """
      self._status = False

  def settLevende(self):
      """ Set the cell status to alive """
      self._status = True

  # Get status
  def erLevende(self):
      """ Return the status of the cell """
      return self._status

  def hentStatusTegn(self):
      """
      Return a "sign" to use on the game board.
      Alive --> "O", Dead --> "."
      """
      if self._status == True:
          return "O"
      elif self._status == False:
          return "."
      else:
          print("Something went wrong")
