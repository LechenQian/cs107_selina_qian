# coder: Selina Qian, listener: Ling Feng, Yichun Yao


# Use a class
class Node:
    def __init__(self, val, der=1):
        self.val = val

        self.der = der

    def __pow__(self, power):


        new_der = power * self.val ** (power - 1)
        new_val = self.val ** power
        return Node(new_val, new_der)


if __name__ == "__main__":
    x = Node(3)
    r = 4
    f = x ** 4
    print(f.val, f.der)
