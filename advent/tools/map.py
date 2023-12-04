from typing import Any

def convert_to_complex(map: list[list[Any]]) -> dict[complex, Any]:
	"""Converts a 2D map to use complex coord.
 
	Note that dictionaries are ordered so you can iterate through this as well.

	Args:
		map (list[list[Any]]): map as 2D array
	"""
	new_map = {}
	for ridx, row in enumerate(map):
		for cidx, ele in enumerate(row):
			new_map[complex(ridx, cidx)] = ele
	return new_map