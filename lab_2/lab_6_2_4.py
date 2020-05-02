#!/usr/bin/env python3

import sys


def _flatten_it(data, history):
	history.append(id(data))
	#
	for element in data:
		if id(element) in history:
			yield None
		elif isinstance(data, dict):
			if isinstance(data[element], dict):
				yield from _flatten_it(data[element], history)
			else:
				yield {element: data[element]}
		elif isinstance(element, (list, dict, tuple)):
			try:
				yield from _flatten_it(element, history)
			except:
				yield None
		else:
			yield element
	history.pop()


def flatten_it(data):
	return _flatten_it(data, [])


if __name__ == "__main__":
	data = {1: {2: 4, 3: {3: 6, 4: 8}}, 5: 10}
	print(data)
	#
	print(list(flatten_it(data)))
