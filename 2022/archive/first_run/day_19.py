import os
from collections import defaultdict
import re


def parse_input(data_file):
	with open(data_file) as f:
		lines = f.readlines()
		robots = []
		for line in lines:
			robot = re.findall(r'\d+', line)
			robot = [int(robot[0]), [int(robot[1]), 0, 0, 0], [int(robot[2]), 0, 0, 0], [
						 int(robot[3]), int(robot[4]), 0, 0], [int(robot[5]), 0, int(robot[6]), 0]]
			robots.append(robot)
	return robots

def get_potential(saway):
	if saway == 0:
		return 0
	return saway + get_potential(saway-1)


# def _main(data_file):
# 	# bp #, or cost, cr cost, or cost x 2, gr cost x 2
# 	robotbps = parse_input(data_file)

# 	global max_resources
# 	max_resources = 0
# 	def traverse(resources: tuple[int, int, int, int], robots: tuple[int, int, int, int], step: int, robotbpr) -> int:
# 		global max_resources
# 		if step >= 25:
# 			max_resources = max(max_resources, resources[3])
# 			return resources[3]
		
# 		# limit by potential: cur res + robots[3]*(25-step) + potential
# 		if max_resources >= (resources[3] + robots[3]*(25-step) + get_potential(24-step)):
# 			return 0

# 		# # get the max needed per robot
# 		mrobneeded = [0,0,0,float("inf")]
# 		for robs in robotbpr:
# 			for idx,i in enumerate(robs):
# 				mrobneeded[idx] = max(mrobneeded[idx], i)

# 		# select robot to be made
# 		maxgeo = resources[3]+(25-step)*robots[3]
# 		for ridx, newrob in enumerate(robotbpr+[[0,0,0,0]]): 
# 			if ridx<len(robots) and (mrobneeded[ridx] <= robots[ridx]):
# 				continue
# 			# check if cur robots can accomodate for next rob
# 			if not all([(nr-ne) <= 0 or pr > 0 for nr, pr,ne in zip(newrob, robots,resources)]): # guarantees we can create newrob
# 				continue
# 			newres = [i-j+k for i,j,k in zip(resources, newrob,robots)]
# 			step = step + 1
# 			maxgeo = max(newres[3],maxgeo)

# 			# get resources O(1)
# 			while any([x < 0 for x in newres]):
# 				newres = [i+j for i,j in zip(newres, robots)]
# 				maxgeo = max(newres[3],maxgeo)
# 				step += 1
# 				if step >= 25:
# 					break
# 			if any([x < 0 for x in newres]):
# 				continue
# 			newrobots = list(robots)
# 			if ridx < 4:
# 				newrobots[ridx] += 1
# 			maxgeo = max(maxgeo, newres[3], traverse(tuple(newres), tuple(newrobots), step, robotbpr))
# 		max_resources = max(max_resources, maxgeo)
# 		return maxgeo
			

# 	cost = 0
# 	for bpr in robotbps:
# 		resources = (1, 0, 0, 0)  # ore, clay, ob, geo
# 		cost+=traverse(resources, (1, 0, 0, 0), 1, bpr[1:])*bpr[0]
# 		print(max_resources)
# 		max_resources = 0
# 	return cost

MAX_STEP=32

def main(data_file):
	# bp #, or cost, cr cost, or cost x 2, gr cost x 2
	robotbps = parse_input(data_file)
	global max_resources
	max_resources = 0
	def traverse(
		resources: tuple[int, int, int, int], 
		robots: tuple[int, int, int, int], 
		step: int,
		add_rob_idx:int,
		robotbpr
	) -> int:
		global max_resources
		step+=1
		if step > MAX_STEP:
			return 0
		newrobots = list(robots)
		newres = [i+k for i,k in zip(resources,robots)]
		if add_rob_idx >= 0:
			# add resources
			newres = [i-j for i,j in zip(newres,robotbpr[add_rob_idx])]
			# add robot if selected
			newrobots[add_rob_idx] += 1
		if newres[3]+newrobots[3]*(MAX_STEP-step)+get_potential(MAX_STEP-step) <= max_resources:
			return 0
		# limit by max robot needed.
		mrobneeded = [0,0,0,float("inf")]
		for robs in robotbpr:
			for idx,i in enumerate(robs):
				mrobneeded[idx] = max(mrobneeded[idx], i)

		# select next robot
		maxgeo = newres[3]+newrobots[3]*(MAX_STEP-step)
		for ridx, potrob in enumerate(robotbpr):
			if newrobots[ridx] >= mrobneeded[ridx]:
				continue
			nnres = newres.copy()
			nstep = step
			# accumulate resources
			while any([i < j for i,j in zip(nnres,potrob)]):
				nstep+=1
				nnres = [i+k for i,k in zip(nnres,newrobots)]
				if nstep > MAX_STEP:
					break
			if any([i < j for i,j in zip(nnres,potrob)]):
				continue
			maxgeo = max(maxgeo,traverse(tuple(nnres),tuple(newrobots),nstep,ridx,robotbpr))
		max_resources = max(max_resources,maxgeo)
		return maxgeo
			

	cost = 1
	for bpr in robotbps:
		resources = (1, 0, 0, 0)  # ore, clay, ob, geo
		cost*=traverse(resources, (1, 0, 0, 0), 1, -1, bpr[1:])
		max_resources = 0
	return cost

SHOW_MAIN = 0
if __name__ == "__main__":
	tout = main('data_19.t')
	eout = 3472
	assert tout == eout, tout
	print("Test Success")
	mout = main('data_19')
	print("main: ", mout)
