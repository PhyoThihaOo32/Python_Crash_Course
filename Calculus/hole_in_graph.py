# A hole is a missing point in the graph of a function, caused by cancellation in a rational function. The function looks continuous everywhere else, but at that one
# x-value, it’s undefined even though the limit exists.

# y = 3(x-2) / (x-2)

x = 2
h = 0.00001

y_right = (3 * ((x + h) - 2)) / ((x + h) - 2)
y_left = (3 * ((x - h) - 2)) / ((x - h) - 2)

print("y_right = ", y_right)
print("y_left = ", y_left)

if round(y_right) != round(y_left):
    print("Limit does not exist at x = ", x)
else:
    print("limit at x = ", x)
