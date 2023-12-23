- part 1 is pretty easy
- part 2 is a tough one
	- I guess the way to generalize the approach for these types of questions is:
		1. try general optimizations given qualities from problem description
		 	- get direction you can use:
				- optimize by constraining to constant input space (compress dimensions that scale to large inputs (eg. using set instead of list))
					- here, we are unable to do this because we would have to keep information about the exact board that the element is in.
				- optimize by finding repeating elements across time
					- this is a valid solution, but the complexity of the logic increases as you're trying to solve multiple random equations.
		2. analyze input (sample/puzzle) for optimizations towards the input that are not discussed
			- input is visualized.
			- perhaps there's commonality in the input which we can use (either sample, or more importantly; main data)
			- keep flow of thought from above going - see if we can introduce some assumptions about the input which would make defining the patterns easier