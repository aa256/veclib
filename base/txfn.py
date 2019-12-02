import math
import typing

from .mat import Mat, I
from .txable import Txable

from .vec import Vec, z


class Txfn:

	class Op:
		def __init__(self, val:typing.Union[Mat, Vec]):
			self.val = val

		def __bool__(self):
			return not (self.val == z or self.val == I)

		def __mul__(self, vec):
			if isinstance(self.val, Vec):
				return self.val + vec
			elif isinstance(self.val, Mat):
				return self.val*vec
			raise ValueError("Unexpected operator value: {}\n".format(self.val))

		def __matmul__(self, op):
			"""
			Joins two operations of the same type.
			"""
			if not isinstance(self.val, type(op.val)):
				raise ValueError("@ operator only combines Operations of the same type")
			if isinstance(self.val, Vec):
				return self.Op(self.val + op.val)
			elif isinstance(self.val, Mat):
				return self.Op(self.val * op.val)
			print("HOOHOO")
			print("{} {}".format(self.val, op.val))
			raise ValueError("This should never happen")

		def __inv__(self):
			if isinstance(self.val, Vec):
				return self.Op(-self.val)
			elif isinstance(self.val, Mat):
				return self.Op(~self.val)

		@staticmethod
		def swap_left(pre, mat, pos):
			return pre+mat*pos, mat

		@staticmethod
		def swap_right(pre, mat, pos):
			return mat, ~mat*pre + pos

	def __init__(self, *ops:typing.Union[Mat, Vec, Op]):
		"""
		Transformations read in order of right to left.

		Invariant: ops are not adjacent.
		"""
		[print(str(op)) for op in ops]
		for op in ops:
			print(op)

		ops = [self.Op(op) for op in ops]
		ops = [op for op in ops if op]
		if len(ops) == 0:
			self.ops = ops
			return

		prev_op = ops[0]
		out = []
		for i in range(1, len(ops)):
			op = ops[i]
			if type(op.val) is type(prev_op.val):
				prev_op @= op
			else:
				out.append(prev_op)
				prev_op = op
		out.append(prev_op)
		self.ops = tuple(out)

	def __invert__(self):
		return Txfn((~self.op[i]).val for i in range(len(self.ops)-1,-1,-1))

	def __mul__(self, other):
		if isinstance(other, Vec):
			out = other
			for i in range(len(self.ops)-1, -1, -1):
				out = self.ops[i]*out
			return out
		elif isinstance(other, Txable):
			return other.transform(self)
		elif isinstance(other, Txfn):
			outvals = [op.val for op in self.ops]
			outvals.extend([op.val for op in other.ops])
			return Txfn(*outvals)

	def flatten(self, left=True, lazy=True):

		# pre, mat, post
		pre = z
		mat = I
		post = z

		if left:
			for op in self.ops:
				if isinstance(op.val, Vec):
					post += op.val
				elif isinstance(op.val, Mat):
					pre, mat = self.Op.swap_left(pre, mat, post)
					mat *= op.val
					post == z
				else:
					raise ValueError("Unexpected Op val type {}".format(type(op.val)))
		else:
			for op in [self.ops[i] for i in range(len(self.ops)-1, -1, -1)]:
				if isinstance(op.val) == Vec.type:
					post += op.val
				elif type(op.val) == Mat:
					mat, post = self.Op.swap_right(pre, mat, post)
					mat *= op.val
					pre = z
				else:
					raise ValueError("Unexpected Op val type {}".format(type(op.val)))

		if lazy:
			return Txfn(pre, mat, post)
		elif left:
			return Txfn(self.Op.swap_left(pre, mat, post))
		return Txfn(self.Op.swap_right(pre, mat, post))

	@staticmethod
	def rotate_int(b, a=1, ctr=z):
		return Txfn(ctr, mat, -ctr)

	def rotate(frac, ctr=z):
		c = math.cos(2*math.pi*frac)
		s = math.sin(2*math.pi*frac)
		mat = Mat(c, -s, s, c)
		return Txfn(ctr, mat, -ctr)

	@staticmethod
	def scale(s, ctr=z):
		return Txfn(ctr, Mat(s, 0, 0, s), -ctr)
