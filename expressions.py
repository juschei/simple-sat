from abc import ABC, abstractmethod

class Expression(ABC):

	@abstractmethod
	def simplify(self):
		print("HERE")
		pass

	def fully_simplify(self):
		expr = self
		while expr not in [True, False]:
			expr_simplified = expr.simplify()
			print("expr", expr)
			if str(expr) == str(expr_simplified):
				return expr
			expr = expr_simplified
		return expr

class Variable(Expression):
	def __init__(self, name, value=None):
		self.name = name
		self.value = value

	# Assumes that value will only be set
	# to boolean values 
	def evaluate(self):
		if self.value == None:
			return None
		else:
			assert type(self.value) == type(True)
			return self.value

	def simplify(self):
		return self

	def __str__(self):
		if self.value == None:
			return self.name
		else:
			assert type(self.value) == type(True)
			return str(self.value)

class NOT(Expression):
	def __init__(self, exp):
		self.exp = exp

	def evaluate(self):
		exp_eval = self.exp.evaluate()
		if exp_eval == None:
			return None
		else:
			assert type(exp_eval) == type(True)
			return not exp_eval

	def simplify(self):
		exp_eval = self.exp.evaluate()
		if exp_eval == None:
			return NOT(self.exp.simplify())
		else:
			assert type(exp_eval) == type(True)
			return exp_eval


	def __str__(self):
		return "(" + "¬" + str(self.exp) + ")"

class AND(Expression):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self):
		left_eval = self.left.evaluate()
		right_eval = self.right.evaluate()

		if left_eval == None or right_eval == None:
			return None
		else:
			return left_eval and right_eval

	def simplify(self):
		left_eval = self.left.evaluate()
		right_eval = self.right.evaluate()

		if left_eval == None and right_eval == None:
			return AND(self.left.simplify(), self.right.simplify())

		if left_eval == 0 or right_eval == 0:
			return Variable(None, False)
		elif left_eval == 1 and right_eval == 1:
			return Variable(None, True)
		elif left_eval == 1:
			return self.right.simplify()
		elif right_eval == 1:
			return self.left.simplify()


	# TODO implement proper parentheses
	def __str__(self):
		return "(" + str(self.left) + "∧" + str(self.right) + ")"

class OR(Expression):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def simplify(self):
		pass

	def evaluate(self):
		left_eval = self.left.evaluate()
		right_eval = self.right.evaluate()

		if left_eval == None or right_eval == None:
			return None
		else:
			return left_eval or right_eval

	def simplify(self):
		left_eval = self.left.evaluate()
		right_eval = self.right.evaluate()

		#print(str(self.left) + " evaluates to " + str(left_eval))
		#print(str(self.right) + " evaluates to " + str(right_eval))

		if left_eval == None and right_eval == None:
			return OR(self.left.simplify(), self.right.simplify())

		if left_eval == 0 and right_eval == 0:
			return Variable(None, False)
		elif left_eval == 1 or right_eval == 1:
			return Variable(None, True)
		elif left_eval == 0:
			return self.right.simplify()
		elif right_eval == 0:
			return self.left.simplify()
			
	def __str__(self):
		return "(" + str(self.left) + "∨" + str(self.right) + ")"


if __name__ == "__main__":

	A = Variable("A")
	B = Variable("B")
	C = Variable("C")

	expression = NOT(AND(OR(NOT(A), B), AND(NOT(A), AND(B, C))))

	B.value = False
	print()
	print(expression)
	print(expression.fully_simplify())
	print()

	B.value = None
	C.value = True
	print(expression)
	print(expression.fully_simplify())