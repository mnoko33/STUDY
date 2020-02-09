class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# linked_list에 있어야하는 것: push, delete, insert, 
class linked_list:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        ans = ""
        node = self.root
        while node:
            ans += f' {node.data}'
            node = node.next
        return(ans)

    def push(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            node = self.root
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, del_data):
        if self.root.data == del_data:
            del_node = self.root
            self.root = self.root.next
            del del_node
            print('delete target node') 
        else:
            before_node = self.root
            node = self.root.next
            while True:
                if node.data == del_data:
                    del_node = node
                    before_node.next = node.next
                    del del_node
                    print('delete target node') 
                    break
                else:
                    before_node = node
                    node = node.next
                    
linked_list = linked_list()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
print('linked_list :', linked_list)
linked_list.delete(2)
print('linked_list :', linked_list)
linked_list.delete(1)
print('linked_list :', linked_list)