Day       Time  Rank  Score       Time   Rank  Score
  7   00:32:44  2958      0   01:00:55   3801      0

- Not good. Missed a lot of cases trying to read quickly.
- Next time, go slower, see if you can validate each of the rules provided.
- code is super ugly
- there was some uncertainty felt when doing getting the edgecase - I didn't immediately realize the problem and had to probe for a while. Try the step below:

New Approach:
- Once requirements change - take the time to re-evaluate it's affect on the rules that were previously validated.
	- see which functions this rule change affects, and then redo code and validate for new rules

New Mindset:
- Assume that per cycle, I won't change in terms of accuracy of intuition. Intuition affects the following abilities (and additionally, intuition tells you when purely relying on intuition starts to crumble, and you need a way of noting things down - otherwise, your intuition will crumble and you wouldn't even know):
	- quick discernment of important information pertaining to rules 
		- unreliable, needs solution
	- which rules are affected once problem shifts
		unreliable, needs solution
	- finding which places of code to change given new requirements
		- reliable with some more practice, gained through previous cycle of AOC
	- understand overall, general solution on reading problem
		- reliable, gained through normal coding
- also note that relying on intuition won't actually make your intuition better, and therefore you won't improve quickly
- I think that for this round of AOC, we can reasonably expect that I won't change in terms of this intuition
- so don't rely on intuition for the points above, especially now since the problems are getting a bit more complex (before was ok, but now, don't risk it)
- Instead, use jot notes. For a detailed approach do the following:
	1. identify rules and note them down somewhere
	2. convert these rules to example inputs cases (you might not need to run tests, but at least keep them in mind)
	3. when writing code, make sure logic conforms to examples (you don't have to run through end to end, but at least test the important logic)
	4. (for changes to rules) Draw out fully the scope of impact of the rules affected
		- add new cases for these affected, and see where (and how) your code can be changed to cover these cases cleanly (this identifying in code can be done through intuition since this intuition seemed to have been gained during the previous AoC cycle: aka, find the function that fits the best, find the change that is the least intrusive)
		- run through code to make sure code changes cover these new (and old) cases
- hopefully, by the end of this cycle, the intuition will build up such that during the next cycle, this jot note process will become intuition. Here is the expected way of it becoming intuition:
	1. there will be confusion about the scope of what to jot down, and what is ok to use intuition for in practice, and there will still be some rough patches (though there should be less than before)
	2. jot note takes a long time and is inefficient
	3. jot note becomes more efficient and starts aiding the process, taking load off of relying on intuition (still might be inefficient)
	4. increase in efficiency:
		- jot note becomes highly optimzed and only a few key items need to be noted down (gained intuition for identifying key rules) (note: step 4, 5 are interchangable)
		- gets faster at converting jot notes to code (note: step 4, 5 are interchangable)
	6. starts jotting down inbetween code as comments (no longer needs paper for larger design) -- this is already a good state
	7. no longer needs comments and can represent the cases using code
	8. no longer needs to write down all cases at once and just write code sequentially for cases
