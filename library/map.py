from typing import Any

def convert_to_complex(map: list[list[Any]]) -> dict[complex, Any]:
	"""Converts a 2D map to use complex coord.

	Args:
		map (list[list[Any]]): map as 2D array
	"""
	new_map = {}
	for ridx, row in map:
		for cidx, ele in row:
			new_map[complex(ridx, cidx)] = ele
	return new_map