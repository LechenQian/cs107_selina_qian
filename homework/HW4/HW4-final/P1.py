import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, h):
    def compute(x):
        diff = (f(h + x) - f(x)) / h
        return diff

    return compute


xs = np.linspace(0.2, 0.4, 1000)
f = np.log
comp_diff_1 = numerical_diff(f, 10 ** (-1))
comp_diff_7 = numerical_diff(f, 10 ** (-7))
comp_diff_15 = numerical_diff(f, 10 ** (-15))

anal_diff = []
num_diff_1 = []
num_diff_7 = []
num_diff_15 = []

for x in xs:
    anal_diff.append(1 / x)
    num_diff_1.append(comp_diff_1(x))
    num_diff_7.append(comp_diff_7(x))
    num_diff_15.append(comp_diff_15(x))

plt.figure()
plt.plot(xs, anal_diff, label='analytical derivative')
plt.plot(xs, num_diff_1, label=r'numerical diff: -1')
plt.plot(xs, num_diff_7, label=r'numerical diff: -7')
plt.plot(xs, num_diff_15, label=r'numerical diff: -15')
plt.xlabel('x')
plt.ylabel('value')
plt.title('Compare the Finite Difference to the True Derivative')
plt.legend()
plt.savefig('P1_fig.png')

print('Answer to Q-a: When h equals 10^(-7), the numerical '
      'differetiation most closely approximates the true derivative. '
      'When h is too small, numerical differentiation can introduce round-off errors in the discretization process and cancellation'
      '; When h is too large, the approximation is not even close to the true derivative.')
print('Answer to Q-b:In auto-differentiation, we apply the chain rule repeatedly to step by step operations so that derivatives can be computed automatically and accurately to working precision.')

plt.show()
