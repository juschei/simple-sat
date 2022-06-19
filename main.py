from expressions import *
from normalforms import *

if __name__ == "__main__":


	A = Variable("A")
	B = Variable("B")
	C = Variable("C")

	expression = NOT(AND(OR(NOT(A), B), AND(NOT(A), AND(B, C))))

	s = str(canonical_dnf(expression, [A, B, C]))
	print(dnf_str_refactor(s))

	s = str(canonical_cnf(expression, [A, B, C]))
	print(cnf_str_refactor(s))
	print(s)