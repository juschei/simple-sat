from expressions import *
from itertools import product


def canonical_dnf(exp: Expression, varlist: list) -> Expression:
	n = len(varlist)
	ever_true = False
	exprs = []
	for values in product([False, True], repeat = n):
		apply_values(varlist, values)
		value = exp.evaluate()
		#reset_values(varlist)

		if value == True:
			ever_true = True
			assert n != 0
			and_expression = varlist[0] if values[0] == True else NOT(varlist[0])
			for i in range(1, n):
				to_and = varlist[i] if values[i] == True else NOT(varlist[i])
				and_expression = AND(and_expression, to_and)
			exprs.append(and_expression)

	# need to reset the values, otherwise the __str__
	# method of variable will replace the names by 
	# the values
	reset_values(varlist)
	if not ever_true:
		return Variable(None, value=False)

	else:
		return multi_or(exprs)		
	
def canonical_cnf(exp: Expression, varlist: list) -> Expression:
	n = len(varlist)
	ever_false = False
	exprs = []
	for values in product([False, True], repeat = n):
		apply_values(varlist, values)
		value = exp.evaluate()
		#reset_values(varlist)

		if value == False:
			ever_false = True
			assert n != 0
			or_expression = NOT(varlist[0]) if values[0] == True else varlist[0]
			for i in range(1, n):
				to_or = NOT(varlist[i]) if values[i] == True else varlist[i]
				or_expression = OR(or_expression, to_or)
			exprs.append(or_expression)

	# need to reset the values, otherwise the __str__
	# method of variable will replace the names by 
	# the values
	reset_values(varlist)
	if not ever_false:
		return Variable(None, value=True)

	else:
		return multi_and(exprs)	

# removes unecessary parenthesis, given that
# cnfstr is the string of an expression in cnf
def dnf_str_refactor(cnfstr : str) -> str:
	cnfstr = cnfstr.replace("(", "").replace(")", "")

	refactored = "("
	for c in cnfstr:
		if c == "∨":
			refactored += ")∨("
		else:
			refactored += c
	return refactored + ")"


def cnf_str_refactor(cnfstr : str) -> str:
	cnfstr = cnfstr.replace("(", "").replace(")", "")

	refactored = "("
	for c in cnfstr:
		if c == "∧":
			refactored += ")∧("
		else:
			refactored += c
	return refactored + ")"

def multi_or(exprs: list) -> Expression:
	assert len(exprs) != 0
	or_expression = exprs[0]
	for i in range(1, len(exprs)):
		or_expression = OR(or_expression, exprs[i])
	return or_expression


def multi_and(exprs: list) -> Expression:
	assert len(exprs) != 0
	and_expression = exprs[0]
	for i in range(1, len(exprs)):
		and_expression = AND(and_expression, exprs[i])
	return and_expression


def print_truth_table(exp: Expression, varlist: list) -> Expression:
	n = len(varlist)
	for values in product([False, True], repeat = n):
		apply_values(varlist, values)
		print("f" + str(values) + " = " + str(exp.evaluate()))
	reset_values(varlist)


def apply_values(varlist: list, values: list) -> None:
	assert len(varlist) == len(values)
	for i in range(len(varlist)):
		varlist[i].value = values[i]


def reset_values(varlist: list) -> None:
	for i in range(len(varlist)):
		varlist[i].value = None
