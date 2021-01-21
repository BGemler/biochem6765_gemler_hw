import csv
from fitting import model_fit


def load_data(data_loc):
	"""
	"""
	ls, monomers, tetramers = [], [], []
	with open(data_loc, "r") as f:
		reader = csv.reader(f)
		next(reader, None)
		next(reader, None)

		for row in reader:
			ls.append(float(row[0]))
			monomers.append(float(row[1]))
			tetramers.append(float(row[2]))
	f.close()

	return ls, monomers, tetramers


def main(data_loc):
	"""
	"""
	ls, monomers, tetramers = load_data(data_loc)
	k0, n0 = 1, 1

	# fit & plot monomers
	model_fit(ls, monomers, k0, n0, "hyperbolic", "monomer")
	model_fit(ls, monomers, k0, n0, "hill", "monomer")

	# fit & plot tetramers
	model_fit(ls, tetramers, k0, n0, "hyperbolic", "tetramer")
	model_fit(ls, tetramers, k0, n0, "hill", "tetramer")

	return


data_loc = "resources/binding-data-1.csv"

main(data_loc)