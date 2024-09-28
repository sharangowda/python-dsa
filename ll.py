class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_value(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print(f"The length is {self.length}")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head == new_node
            self.tail == new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head == new_node
            self.tail == new_node
        prev = self.head
        self.head = new_node
        self.head.next = prev
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        pre = self.tail
        self.length -= 1

    def pop_first(self):
        if self.length == 1:
            return None
        pre = self.head
        next = self.head.next
        self.head = next
        pre.next = None
        self.length -= 1
        if self.length == 1:
            return self.tail

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        if 0 < index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        pre = self.get(index - 1)
        new_node = Node(value)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        # new_node = Node(value)
        # temp = self.get(index - 1)
        # new_node.next = temp.next
        # temp.next = new_node
        # self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index - 1)
        temp = self.get(index)
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True


new_ll = LinkedList(4)
new_ll.append(5)
new_ll.append(6)
new_ll.append(7)
new_ll.prepend(3)
new_ll.prepend(2)
new_ll.prepend(1)
new_ll.insert(6, 10)
new_ll.print_value()
print("-------------------------------------------------------------")
new_ll.remove(6)
new_ll.print_value()
print("-------------------------------------------------------------")
