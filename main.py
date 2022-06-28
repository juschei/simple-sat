from expressions import *
from normalforms import *
import copy


if __name__ == "__main__":


	A = Variable("A")
	B = Variable("B")
	C = Variable("C")

	expression = NOT(AND(OR(NOT(A), B), AND(NOT(A), AND(B, C))))

	dnf = canonical_cnf(expression, [A, B, C])
	print(cnf_str_refactor(str(dnf)))
	print(dnf)

	print_truth_table(expression, [A, B, C])

	print()

	print(dnf.left)
	print(dnf.right)

	a = copy.deepcopy(dnf)
	print(a)
	a.left = NOT(C)
	print()
	print(dnf)
	dnf2 = AND(dnf, OR(A, NOT(B)))
	print(dnf2)
	varname_mapping = {"A": 1, "B": 2, "C": 3}
	print(convert_dnf_format(dnf2, varname_mapping))

