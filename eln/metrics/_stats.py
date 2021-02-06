from scipy.stats import ttest_ind

def t_test(a,b):

	"""Performed a t-test on two samples

	Parameters
	----------
	a,b: arrays of values to be used for the t-test

	Returns
	-------
	t: t-value
    p: two-tailed p value

	Examples
	--------

	"""
	t = ttest_ind(a, b)

	return t
