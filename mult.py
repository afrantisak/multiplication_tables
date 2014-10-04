#!/bin/env python
import sys
import random

maxint = 12
maxwidth = 3

def generate_number(N):
    return random.randint(1, N)

def generate_multiplication_problem():
    a = random.randint(1, maxint)
    b = random.randint(1, maxint)
    return a, b, a * b

def generate_problem_grid():
    problem_grid = []
    for y in range(5):
        problem_row = []
        for x in range(5):
            problem = generate_multiplication_problem()
            problem_row.append(problem)
        problem_grid.append(problem_row)
    return problem_grid

def format_problem(problem):
    return "{a:{w}d} x {b:{w}d} = {c:{w}s}  ".format(a=problem[0], b=problem[1], c="", w=maxwidth)

def format_solution(problem):
    return "{a:{w}d} x {b:{w}d} = {c:{w}d}  ".format(a=problem[0], b=problem[1], c=problem[2], w=maxwidth)
        
grid = generate_problem_grid()

print "PROBLEMS:"
for y in range(len(grid)):
    line = ''
    for x in range(len(grid[y])):
        line += format_problem(grid[y][x])
    print line

print "\n" * 5
print "SOLUTIONS:"
for y in range(len(grid)):
    line = ''
    for x in range(len(grid[y])):
        line += format_solution(grid[y][x])
    print line

