Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []


def solution(x):
    return 0