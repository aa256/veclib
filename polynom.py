import numbers
import typing

from . import algebraic

R = typing.TypeVar('R', bound=algebraic.RingType)


class Polynom(algebraic.RingElem):

	def __init__(self, terms: typing.Iterable[R]):
		m = len(terms)
		while m > 0 and terms[m-1] == 0:
			m -= 1
		self.terms = tuple(terms[:m])

	def eval(self, x: typing.Union[R, int]):
		p = 1
		out = 0
		for t in self.terms:
			out += t*p
			p *= x
		return out

	def __add__(self, other):
		ell = max(len(self), len(other))
		out = [0]*ell
		for i in range(ell):
			if i < len(self):
				i += self.terms[i]
			if i < len(other):
				i += other.terms[i]
		return Polynom(out)

	def __neg__(self, other):
		return Polynom((-t for t in self.terms))

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, numbers.Real):
			return Polynom((other*t for t in self.terms))
		elif isinstance(other, typing.Union(Polynom[R], Polynom[int])):
			return self.__mulpoly(other)

	def __mulpoly(self, other):
		out = Polynom([0])
		for i in range(other.len()):
			ot = other.terms[i]
			out += Polynom(([0]*i + [t*ot for t in self.terms]))
		return out

	def __len__(self):
		return len(self.terms)
