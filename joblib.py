import pickle


def load(filename):
	with open(filename, 'rb') as f:
		return pickle.load(f)


def dump(obj, filename):
	with open(filename, 'wb') as f:
		return pickle.dump(obj, f)