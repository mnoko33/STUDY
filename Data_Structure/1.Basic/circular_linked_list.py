class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class circular_linked_list:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert(self, data):
        if not self.root:
            node = Node(data)
            self.root = node
            node.next = self.root
        else:
            node = self.root
            while True:
                if node.next == self.root:
                    break
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.next = self.root
        self.size += 1
        return 

    def isEmpty(self):
        return self.size == 0

    def delete(self, data): # self.data == data인 node를 삭제하기
        if self.isEmpty():
            print('linked_list is empty')
            return 
        node = self.root
        while True:
            if node.next.data == data:
                next = node.next.next
                if node.next == self.root:
                    self.root = next
                del node.next
                node.next = next
                self.size -= 1
                return
            if node.next == self.root:
                print(f'there is no node with {data}')
                break
            node = node.next
            
    
    def __str__(self):
        ans = ""
        node = self.root
        while True:
            ans += f' {node.data}'
            if node.next == self.root:
                break
            node = node.next
        return ans

arr = circular_linked_list()
arr.insert('A')
arr.insert('B')
arr.insert('C')
print('arr :', arr, ' root : ', arr.root.data)
arr.delete('B')
print('arr :', arr, ' root : ', arr.root.data)
arr.insert('D')
arr.insert('E')
print('arr :', arr, ' root : ', arr.root.data)
arr.delete('A')
print('arr :', arr, ' root : ', arr.root.data)
arr.delete('K')
print('arr :', arr, ' root : ', arr.root.data)