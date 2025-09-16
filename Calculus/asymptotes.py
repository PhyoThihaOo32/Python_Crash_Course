# An asymptote is a line that a graph of a function approaches but never quite touches (or only touches in the limit).

# y = 3x^2 / x^2 - 4

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols("x")

# put the equation here
eq = (x**2) - 4

# solve() set the equation to zero
print("x = ", solve(eq, x))

# finding limit approaching from left or right

x = 2
h = 0.00001

# for y = 3x^2 / x^2 - 4

y_right = (3 * (x + h) ** 2) / ((x + h) ** 2 - 4)
y_left = (3 * (x - h) ** 2) / ((x - h) ** 2 - 4)

print("y_right = ", y_right)
print("y_left = ", y_left)

if round(y_right) != round(y_left):
    print("Limit does not exit at x = ", x)
