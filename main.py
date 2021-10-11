from z3 import *

# EBAC = A/(r * Wt) - B * T
# Where:
#   EBAC = BAC
#   A = mass of alcohol consumed
#   r = ratio of body water to total weight, avg 0.68 for men and 0.55 for women
#   Wt = body weight
#   B = rate at which alcohol is metabolised (~0.017%/h)
#   T = time during which alcohol has been present in the blood

EBAC, A, r, Wt, B, T = Reals('EBAC A r Wt B T')
equations = [
    EBAC == A / (r * Wt) - B * T
    ]

# 80kg male drinking 18ml of pure alcohol in 1/2 hour
problem_one = [
    r == 0.68,
    B == 0.017,
    T == 0.5,
    A == 18,
    Wt == 80
]

# 80kg female drinking 18ml of pure alcohol in 1/2 hour
problem_two = [
    r == 0.55,
    B == 0.017,
    T == 0.5,
    A == 18,
    Wt == 80
]

# 120kg male drinking 18ml of pure alcohol in 1/2 hour
problem_three = [
    r == 0.68,
    B == 0.017,
    T == 0.5,
    A == 18,
    Wt == 120
]

# 50kg female drinking 18ml of pure alcohol in 1/2 hour
problem_four = [
    r == 0.55,
    B == 0.017,
    T == 0.5,
    A == 18,
    Wt == 50
]

# 80kg male drinking 18ml of pure alcohol in 2 hours
problem_five = [
    r == 0.68,
    B == 0.017,
    T == 2,
    A == 18,
    Wt == 80
]

# 80kg male drinking 18ml of pure alcohol in 1 day
problem_six = [
    r == 0.68,
    B == 0.017,
    T == 24,
    A == 18,
    Wt == 80
]

# 80kg male drinking no alcohol in 1 hour
problem_seven = [
    r == 0.68,
    B == 0.017,
    T == 1,
    A == 0,
    Wt == 80
]

problems = [
    problem_one,
    problem_two,
    problem_three,
    problem_four,
    problem_five,
    problem_six,
    problem_seven
]


def solve_bac():
    for problem in problems:
        idx = problems.index(problem)

        print(f'Problem {idx}:')
        print(problem)

        print("Solution:")
        solve(equations + problem)

        print("\n")


if __name__ == '__main__':
    solve_bac()
