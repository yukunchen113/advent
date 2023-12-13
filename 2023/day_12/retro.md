Day       Time  Rank  Score       Time   Rank  Score
 12   01:04:37  4476      0   01:45:33   1989      0

- got stuck in edge case hell in the beginning
	- need to find a way to practice saying out of edge case hell.
- could've got pt2 done way sooner if I realized memoization was sufficient from the beginning, instead of trying weird, incorrect optimizations
- optimizations: look at things by their transformations, not objects
	- transformations -> objects -> corner + edge cases
	- to get the transformations, start from what you want to be done to the objects, and objects with similar transformations can be done with the same code (must be obviously the same transformations)
	- as long as your solution completely defines the logic you want it to for positive cases (with a default), edge cases only need to outline cases which will crash the logic, and everything else should fall under the default.