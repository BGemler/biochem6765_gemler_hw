from lmfit import Model # https://lmfit.github.io/lmfit-py/model.html
import matplotlib.pyplot as plt


def hyperbolic_eq(l, k):
	"""
	"""
	y = l / (l + k)

	return y


def hill_eq(l, k, n):
	"""
	"""
	y = (l ** n) / ((l ** n) + (k ** n))

	return y


def plot_result(result, plt_out, model_choice, y_choice, chi_sqr):
	"""
	"""
	result.plot(numpoints = 100)

	plt.title("Y to Fit: " + y_choice + "\n" + \
							"chi-square: " + chi_sqr)
	plt.savefig(plt_out)
	plt.close()

	return


def model_fit(x_data, y_data, k0, n0, model_choice, y_choice):
	"""
	"""
	plt_out = "results/scatter-" + model_choice + "-" + y_choice + ".png"

	if model_choice == "hyperbolic":
		mod = Model(hyperbolic_eq)
		result = mod.fit(y_data, l = x_data, k = k0)
	elif model_choice == "hill":
		mod = Model(hill_eq)
		result = mod.fit(y_data, l = x_data, k = k0, n = n0)

	chi_sqr = ""
	result_report = result.fit_report().split("\n")
	for t in result_report:
		if t.startswith("    chi-square         ="):
			chi_sqr = t.split("    chi-square         =")[1]

	plot_result(result, plt_out, model_choice, y_choice, chi_sqr)

	print("Y-choice: ", y_choice)
	print("Model-choice: ", model_choice)
	print(result.fit_report())
	print('k: {:.3f} ± {:.3f} µM'.format(
    result.params['k'].value,
    result.params['k'].stderr))
	if model_choice == "hill":
		print('n: {:.3f} ± {:.3f}'.format(
	    result.params['n'].value,
	    result.params['n'].stderr))		
	print("\n\n\n\n")

	return