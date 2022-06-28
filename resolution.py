from expressions import *
from normalforms import *


# given two clauses in numerical form, find the smallest variable
# that can be eliminated via resolution
# returns value in a (negative is in b)   # maybe (_, index in a, index in b)
# returns None of not found
def smallest_resolvable_variable(a: list, b: list):
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if a[i] == -b[j]:
			return a[i]
		elif abs(a[i]) <= abs(b[j]):
			i += 1
		elif abs(a[i]) > abs(b[j]):
			j += 1
	return None


# resolves cnf by comparing all clauses and removing redundant
# variables
# TODO deal with special cases like (x) and (not x)
def resolve(cnf: list):
	for i in range(len(cnf)-1):
		for j in range(i+1, len(cnf)):
			a = cnf[i]
			b = cnf[j]
			value = smallest_resolvable_variable(a, b)
			while value != None:
				a.remove(value)
				b.remove(-value)
				value = smallest_resolvable_variable(a, b)


# maybe store which variables are in which lists and only check the
# required ones
def add_clause_with_resolve(cnf: list):

if __name__ == "__main__":

	cnf = [[-1, 2, -3, -6], [2, 3, 4, 5, 6]]

	resolve(cnf)
	print(cnf)