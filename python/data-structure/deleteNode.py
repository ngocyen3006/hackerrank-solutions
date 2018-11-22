# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next

        if node:
            print(sep)


def deleteNode(head, position):
    if position == 0:
        return head.next
    node = head
    i = 0
    while i < position - 1 and node:
        node = node.next
        i += 1
    node.next = node.next.next
    return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())
    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ')
