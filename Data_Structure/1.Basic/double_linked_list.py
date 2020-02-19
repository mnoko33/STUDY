# double linked list
class Node:
    def __init__(self, data, before=None, next=None):
        self.data = data
        self.before = before
        self.next = next

    def __str__(self):
        return f'{self.data}'

class DL:
    def __init__(self, root=None, size=0):
        self.root = root
        self.size = size

    def find(self, target):
        node = self.root
        while True:
            if node.data == target:
                return node
            if node.next:
                node = node.next
            else:
                node
                break
        return False

    def insert(self, new, target):
        self.size +=1
        new = Node(new)
        node = self.find(target)
        print('target : ', node)
        if not node.next:
            node.next = new
            new.before = node
        else:
            next_node = node.next
            next_node.before = new
            new.next = next_node
            new.before = node
            node.next = new
        print(f'insert {new} after {target}')

    def remove(self, target):
        self.size -= 1
        target = self.find(target)
        if target == self.root:
            next_node = target.next
            self.root = next_node
            next_node.before = None
        else:
            before_node = target.before
            next_node = target.next
            
            before_node.next = next_node
            next_node.before = before_node
        print(f'remove {target}')
        del target

    def show(self):
        result = ''
        node = self.root
        if not node.next:
            return
        while node.next:
            result += f'{node.data} <=> '
            node = node.next
        result += f'{node.data} <=> '
        print('double_linked_list : ', result[:-4])

    def get_size(self):
        print('size :', self.size)

test = DL()

test.root = Node(0)
test.size = 1
test.show()
test.get_size()
print()
test.insert(1,0)
test.show()
print()
test.insert(2,1)
test.show()
test.get_size()
print()
test.remove(1)
test.show()
test.get_size()
print()
test.insert(4,0)
test.show()
test.get_size()


