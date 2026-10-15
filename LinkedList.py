class Node:

    def __init__(self,value):
        self.value= value
        self.next= None

class LinkedList:

    def __init__(self):
        self.head = None
        # Initially the list is empty

    def __traverse__(self):
        pass

    # O(n)
    def __contains__(self, value):
        last =self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter +=1
            last = last.next
        return counter


    # O(n) linear runtime
    def append(self, value):
        if self.head is None:
            self.head = Node.value
        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = Node(value)

    # O(1)
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index Out of Bounds")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index Out of Bounds")
                    last =last.next

                new_node  = Node(value)
                new_node_next = last.next
                last.next = new_node

    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass

if __name__ == "__main__":
    pass