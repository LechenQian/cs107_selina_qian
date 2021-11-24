from copy import copy, deepcopy
from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
    def _removemin(self,node):

        if not node:
            return None
        elif not node.left:
            return node.right

        node.left = self. _removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._remove(node.left,key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp_node = deepcopy(node)
            node = self._min(temp_node.right)
            node.left= temp_node.left
            node.right = self._removemin(temp_node.right)

        node.size = 1 + self._size(node.left) + self._size(node.right)

        return node

    def _min(self,node):
        if not node:
            return None
        if not node.left:
            return deepcopy(node)
        else:
            return self._min(node.left)

    @staticmethod
    def _size(node):
        return node.size if node else 0

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3





if __name__ == '__main__':
    # tree = BSTTable()
#     # tree.put(5, 'a')
#     # tree.put(1, 'b')
#     # tree.put(2, 'c')
#     # tree.put(10, 'b')
#     # tree.put(20, 'c')
#     # tree.put(6, 'd')
#     # tree.put(3, 'b')
#     # tree.put(8, 'c')
#     # tree.put(11, 'd')
#     # print(tree)
#     # print(tree._removemin(tree._root))
#     #
#     # tree.remove(10)
#     # print(tree)


