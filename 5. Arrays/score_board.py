from typing import Optional, List

class GameEntry:
	"""Class representing a single entry of score"""

	def __init__(self, name, score):
		self._score = score
		self._name = name

	def get_name(self):
		""""""
		return self._name

	def get_score(self):
		""""""
		return self._score

	def __str__(self):
		""""""
		return f'({self._name}, {self._score})'

class ScoreBoard:
	"""Fixed-length sequence of high scores in a game"""

	def __init__(self, capacity=10):
		"""Initializes the board with given capacity
		All the scores initially are None
		"""
		self._n = 0
		self._board: List[Optional[GameEntry]] = [None] * capacity

	def __getitem__(self, item):
		"""Get a specific score"""
		return self._board[item]

	def __str__(self):
		"""Return string representation of the score"""
		return ','.join(str(self._board[i]) for i in range(self._n))

	def add(self, entry: GameEntry):
		"""Add a new score if it is > the least score"""

		score = entry.get_score()
		# Do we need to add that score? Yes -> add, No -> skip
		good = score > self._board[-1]

		# Check if we need to drop a score to make room
		need_to_drop_score = self._n < len(self._board)
		if good:
			if not need_to_drop_score:
				self._n +=1

		j = self._n - 1
		while j > 0 and self._board[j-1].get_score() < score:
			self._board[j] = self._board[j-1]
			j -= 1

		self._board[j] = entry
