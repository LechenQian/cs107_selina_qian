class AutoDiffToy():
    def _to_real(self, other):
        try:
            return float(other.val)
        except:
            return float(other)

    def __init__(self, val, der=1.0):
        self.val = self._to_real(val)
        self.der = der

    def __add__(self, other):
        new_val = self.val + self._to_real(other)
        return AutoDiffToy(new_val, self.der)

    def __radd__(self, other):
        new_val = self.val + self._to_real(other)
        return AutoDiffToy(new_val, self.der)

    def __mul__(self, other):
        new_val = self.val * self._to_real(other)
        new_der = self.der * self._to_real(other)
        return AutoDiffToy(new_val, new_der)

    def __rmul__(self, other):
        new_val = self.val * self._to_real(other)
        new_der = self.der * self._to_real(other)
        return AutoDiffToy(new_val, new_der)


if __name__ == '__main__':
    # case 1
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)

    alpha = 2.0
    beta = 3.0

    f = x * alpha + beta
    print(f.val, f.der)
    # case 2
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)

    f = alpha * x + beta
    print(f.val, f.der)

    # case 3
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)

    f = beta + alpha * x
    print(f.val, f.der)

    # case 4
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)

    f = beta + x * alpha
    print(f.val, f.der)
