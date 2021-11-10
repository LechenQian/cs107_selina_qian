## coder: Selina Qian; listener: Yuhan Zhang

class Fibonacci:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return FibonacciIterator(self.end)


class FibonacciIterator:
    def __init__(self, end):
        self.end = end
        self.curFib = 1
        self.nextFib = 1
        # You may need to create more attributes

    def __iter__(self):
        return self  # The return value of iter() called on an iterator must be the iterator itself.

    def __next__(self):
        if self.end == 0:
            raise StopIteration()
        else:
            self.end -= 1
            nextFib = self.curFib + self.nextFib
            self.curFib = self.nextFib
            self.nextFib = nextFib

        return self.curFib


if __name__ == '__main__':
    fib = Fibonacci(10)  # Create a Fibonacci iterator called fib that contains 10 terms
    print(list(iter(fib)))
