import os


class Tree:
    def __init__(self, name):
        self._children = []
        self._name = name

    def add_child(self, children):
        self._children.append(children)

    def get_name(self):
        return self._name

    def create_tree(self, path_file):
        with open(path_file, 'r') as f:
            lines = f.readlines()
            stack = []
            for line in lines:
                level = line.count('\t')
                name = line.strip()
                node = Tree(name)
                while len(stack) > level:
                    stack.pop()
                if len(stack) == 0:
                    self.add_child(node)
                else:
                    parent = stack[-1]
                    parent.add_child(node)
                stack.append(node)
        return self

    def print_tree(self):
        print(self.get_name())
        for child in self._children:
            child.print_tree()

    def create_folder(self, parent=""):
        if parent:
            path = os.path.join(self.get_name(), parent)
        else:
            path = self.get_name()
        os.makedirs(path, exist_ok=True)
        for child in self._children:
            parent = os.path.join(path, child.get_name())
            child.create_folder(parent)
