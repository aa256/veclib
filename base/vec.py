import math
import numbers
import typing

from . import algebraic
R = typing.TypeVar('R', bound=algebraic.RingType)

class Vec(typing.Generic[R]):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@classmethod
	def by_polar_form(cls, rad, phi):
		x = rad*math.cos(phi)
		y = rad*math.sin(phi)
		return Vec(x,y)

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def __add__(self, other):
		return Vec(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y

	def __neg__(self):
		return Vec(-self.x, -self.y)

	def __sub__(self, other):
		return self + (-other)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y

	def __mul__(self, other):
		if isinstance(other, Vec):
			return Vec(self.x*other.x, self.y*other.y)
		if isinstance(other, numbers.Real):
			return self * Vec.from_real(other)

	@classmethod
	def from_real(cls, x:numbers.Real):
		return Vec(x, x)

	def __truediv__(self, other):
		if isinstance(other, numbers.Number):
			return Vec(self.x/other, self.y/other)

	def len(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

	def phi(self):
		return math.atan2(self.y, self.x)

z = Vec(0,0)