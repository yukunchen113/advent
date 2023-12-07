Day       Time  Rank  Score       Time   Rank  Score
  1   00:05:24  2358      0   00:23:36   2282      0

day 1 retro:

Q1:
- first attempted solution succeeded.
- should get after at typing/less typos

Q2:
- solution failed. Didn't account for overlapping numbers
- it was non obvious from problem description, but after thinking about it, overlapping characters would fit the description better.
- way that I found out was to just code it up after first submission failed
	- I was uncertain whether it was a bug in my code or if my interpretation was wrong
	- aka I knew that my code didn't support overlapping, but didn't know if I should support it
	- this hesitation slowed me down significantly
	- should've just tried it, but also even better - given the overlapping assumption, can the problem be interpreted that same way.
		- this is a bit of a mindset change
- for future reference - you can use overlapped = True for regex library (not re).