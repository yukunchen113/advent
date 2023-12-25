import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex
from skspatial.objects import Line, Points
from numpy import array, cross
from numpy.linalg import solve, norm
from z3 import *

# @mark.solution(test=None)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    stones = []
    for line in data:
        pos, vel = line.split(" @ ")
        pos = np.array([int(i) for i in pos.split(", ")])
        vel = np.array([int(i) for i in vel.split(", ")])
        stones.append((pos, vel))
    output = 0
    least, most = 200000000000000, 400000000000000
    for idx, (p1, v1) in enumerate(stones[:-1]):
        for p2, v2 in stones[idx+1:]:
            m1,m3,_ = v1
            m2,m4,_ = v2
            b1,b3,_ = p1
            b2,b4,_ = p2
            beta = (m1*(b4-b3)/(m3*m2) + (b1-b2)/m2)/(1-m1*m4/(m2*m3))
            x,y = m2*beta+b2,m4*beta+b4
            alpha= (m4*beta+b4-b3)/m3
            output += least<=x<=most and least<=y<=most and alpha>=0 and beta >=0
    return output

def is_intersect_xy(p1,v1,p2,v2,least=-float("inf"),most=float("inf")):
    m1,m3,_ = v1
    m2,m4,_ = v2
    b1,b3,_ = p1
    b2,b4,_ = p2
    beta = (m1*(b4-b3)/(m3*m2) + (b1-b2)/m2)/(1-m1*m4/(m2*m3))
    x,y = m2*beta+b2,m4*beta+b4
    alpha= (m4*beta+b4-b3)/m3
    return x,y,alpha,beta

@mark.solution(test=None)
def pt2_z3(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    stones = []
    for line in data:
        pos, vel = line.split(" @ ")
        pos = [int(i) for i in pos.split(", ")]
        vel = [int(i) for i in vel.split(", ")]
        stones.append((pos, vel))
    
    x,y,z = Int("x"),Int("y"),Int("z")
    vx,vy,vz = Int("vx"),Int("vy"),Int("vz")
    solver = Solver()
    for idx,(pos,vel) in enumerate(stones):
        t = Int(f"T{idx}")
        solver.add(x+t*vx == pos[0]+vel[0]*t)
        solver.add(y+t*vy == pos[1]+vel[1]*t)
        solver.add(z+t*vz == pos[2]+vel[2]*t)
    m = solver.check()
    m = solver.model()
    return m.eval(x+y+z)
    
        
    
    

# @mark.solution(test=None)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    stones = []
    for line in data:
        pos, vel = line.split(" @ ")
        pos = [int(i) for i in pos.split(", ")]
        vel = [int(i) for i in vel.split(", ")]
        stones.append((pos, vel))
    
    # get 3 stones with same xvel, sorted by initial x
    avel = []
    for axis in range(3):
        nstones = defaultdict(list)
        for pos,vel in stones:
            nstones[vel[axis]].append((pos,vel))
        assert nstones
        valid_vel = None
        for _,s in nstones.items():
            if len(s) < 2: continue
            p1,_ = s[0]
            p2,v2 = s[1]
            vel = {n for n in range(-1000, 1000) 
                if n-v2[axis] and not (p2[axis] - p1[axis])%(n-v2[axis])}
            if valid_vel is None:
                valid_vel = vel
            else:
                valid_vel = valid_vel & vel
        assert len(valid_vel) == 1
        avel.append(valid_vel.pop())
    
    # get pos: assume crosses line at t=1 (we can adjust later)
    # I have no idea how to get the position given velocities
    # I don't understand what https://topaz.github.io/paste/#XQAAAQAUDAAAAAAAAAA0m0pnuFI8c914retSmoIG4DZEdJ50slbD81JvM5mQSTreyJmJdG5ErENvWrbR2IGVD6L23kMHykcRMgYleThe4um56yMUrQ/uHrF3HuwBAoalVRDpkkpZviPXlbzmoSJoN4HPLXXSEz4to1kWUxZqDAP0KgxHB8lNPronrj59GR1o5RqFHlyAaZKCkCt0CT05d5nlzaQEh7vz9YXrWsW2L7GNJy0xlJasMTNGvbHeDPXyJItiHXa3MseDaV2MWdvPtI54e9x9dNc4x0wcP85QR7YrlVSs0zCm5rXLsb1nwhxW3xodqj8NIsH0KEVTE+RsDEuy9p9GD7XMP3k/ijz+cL4XqNUA16WFns+o63OLK8vjoiOK5hNuNhurOMMPFIZW6J4Gcf1a64jhwzu9ISgbCXSSR+Bds+Enp5Nwbt7ZwZ1dQ+Ht3zQ4fZeC6auWvC1ES+fsaFDO3vNSXhoUvOqqnk7jkpTDnwCCI3BDrpwD4ixNe9OOP3MMecfv0uWuZYp7IIgsVCQVXIFVmmhvdhQsZ0FmfBcbvK04YE8RMztc7U2dJ4gWw/yF69/CppBSQCPH4Kn0ZCtn0uYJiJXq9BbA7QiokCY4P+rK9k1S0QqL2nlmI1BqIZkboC3A/kV12oqDIfxCn3sylSN/NDGoXUhFaF+fwn7Q4tfyE9xnARW+3AxntYM6cMwc8ZcyyOlBnrM4iJgPsXteSvwdXl5b8YwEpUc/h+Y5JQp1PnFALM6GLx/q85mWShC+xF6KYfcJ4oWboeIVN9TYKhLU8m+MPFnqitqskmfRvaPb8LfK3OSdRFDZUg5N+wrGfxcdg8EtttL+/94x+9FAVz31BpkHQtwS5aMlUr1TpLphUbzn862x9UwmDlR3vhWBr/OeZ2FlQO3F01yGuH5MRytgVH7GHGDipyh7lXLjHA8L5RjuDDUZa7/gHUYHx0iW3dz7dC2bsSiWBpgAMP5YVdQhJMbVYyhP68Nw1H7hmHqwXB4u8k4QuXHeetPd3Z9lSUG4KSpjwy5ePYMdLaLI2KM1GInxXo3MC3rtKFvEr0NyV7ifJ8YBsmu9h26z8bv8qRN8SFBQ/IPrIcdrQI4AHXDg1hDr2641UlRFVGDTDebMhcKlR2nUEdko6UyNvb6FrmiwQTIGZT7E2Gb+X02v+DoWEaxLcG1Imdt6j/Tl9+PmcCa0P3V7/ucxC9GOAerwTAfcDEAhaUYOco9a0nxdRLDc9qbn8Fc3rvjsvTIoTwgykwqraj6xMWBdsCYs1/+CY+8A 
    # is doing to get them, so this solution will be put on pause
            
        
    
    # for t in range(100):
    #     if not len(stones): break
    #     zstones = []
    #     for idx, (pos,vel) in enumerate(stones):
    #         zstones.append((
    #             pos[0] + t*vel[0], 
    #             pos[1] + t*vel[1],
    #             pos[2] + t*vel[2],
    #             idx))
    #     print(zstones)
    #     exit()

        
    # points = Points(points)
    # print(points)
    # line_fit = Line.best_fit(points)
    # pos2, vec2 = line_fit.point, line_fit.direction
    # print(line_fit)
    
        
        
        