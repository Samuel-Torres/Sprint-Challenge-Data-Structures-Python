class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if nothing then return none
        if node is None:
            return None
        # assign the starting node to the incoming node
        current_node = node
        # if the current node's next node isn't empty then run the following code
        if current_node.next_node is not None:
            # keep track of the prev iteration
            prev_node = current_node
            # get the current node that is being iterated through this code's next node
            next_node = current_node.get_next()
            # assign the previous node's next node to to this node's next node
            prev_node.next_node = next_node.next_node
            # this node's next node is the current head... places this node before the head node
            next_node.next_node = self.head
            # assign this node as the head officially moving the head pointer to the node that was moved to the head.
            self.head = next_node
            # this tracks the initial head node all the way to the end and when it gets to the ends break the loop since this node won't have a next node
            current_node = prev_node
            # Recurrssion so that this continues to loop until the initial head node next node is none.
            self.reverse_list(current_node, None)
            # secondary break
        elif current_node is None:
            return
