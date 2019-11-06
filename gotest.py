import random
import ipdb

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Algorithm:
    def __init__(self, number_list):
        self.root = None
        for node in number_list:
            self.insert(node)

    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return

    def search(self, search):
        searcher = self._search_bool(search)
        if searcher is None:
            print("Search target is not found.")
        elif searcher == True:
            print(str(search) + " is found!")
        elif searcher == False:
            print(str(search) + " is not found.")

    def _search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.data == search:
                    return True
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return False

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def deletemin(self, node):
        parent = node
        tmp = node.right
        while tmp.left:
            parent = tmp
            tmp = tmp.left
        parent.right = tmp.right
        return tmp
 
    def delete(self, data):
        node = self.root
        parent = node
        flag = None
        while node:
            if node.data == data:
                if node.left == None and node.right == None:
                    if flag == "left":
                        parent.left = None
                    else:
                        parent.right = None
                elif node.left == None:
                    if flag == "left":
                        parent.left = node.right
                    else:
                        parent.right = node.right
                elif node.right == None:
                    if flag == "left":
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    tmp = self.deletemin(node)
                    if flag == "left":
                        parent.left = tmp
                    else:
                        parent.right = tmp
                    tmp.right = node.right
                    tmp.left = node.left
            parent = node
            if node.data > data:
                node = node.left
                flag = "left"
            else:
                node = node.right
                flag = "right"
ipdb.set_trace()
