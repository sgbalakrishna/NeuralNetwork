x_old = 0
x_new = 5
gamma = 0.0001  # step size
iter = 1
precision = 0.00001


def f(x):
    y = 4 * (x ** 3) - 9 * x ** 2 +7*x -9
    return y


while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new += -gamma * f(x_old)
    iter += 1
    print "iteration", iter

print("minimum occurs at %f" % x_new)
