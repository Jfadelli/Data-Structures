"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        current_head = self.head
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = current_head
            new_node.prev = None
            current_head.prev = new_node
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            head_val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_val
        else: 
            current_head = self.head
            new_head = self.head.next
            current_head.next = None
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return current_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        current_tail = self.tail
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_tail.next = new_node
            new_node.prev = current_tail
            new_node.next = None
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None

        elif self.length ==1:
            tail_val = self.tail.value
            self.head = None
            self.tail = None
            self.length -=1
            return tail_val

        else:
            curr_tail = self.tail
            new_tail = curr_tail.prev   
            curr_tail.prev = None
            new_tail.next = None
            self.tail = new_tail
            self.length -=1
            return curr_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        curr_head = self.head
        curr_tail= self.tail
        if self.length ==0:
            return None
        elif self.length ==1:
            self.head = node
            self.tail=node
        elif self.length ==2:
            curr_head = self.head
            curr_tail = self.tail
            curr_tail.next = curr_head
            curr_tail.prev = None
            self.head = curr_tail
            curr_head.prev = self.head
            curr_head.next = None
            self.tail = curr_head

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = curr_head
            curr_head.prev = node
            self.head = node
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length ==0:
            return None
        elif self.length ==1:
            self.head = node
            self.tail = node
        elif self.length ==2:
            curr_head = self.head
            curr_tail = self.tail
            self.tail.next = curr_head
            curr_head.next = None
            curr_head.prev = self.tail
            self.head = curr_tail
            self.tail = curr_head
        else:
            # node.prev.next = node.next
            # node.next.prev = node.prev
            curr_tail = self.tail
            curr_tail.next = node
            node.prev = curr_tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return None

        if node == self.head:
            self.remove_from_head()

        elif node == self.tail:
            self.remove_from_tail()

        else:
            prev_node = node.prev
            next_node = node.next   
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -=1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = 0
        current = self.head

        if self.head.next is None:
            return self.head.value

        else:

            while current  is not None :
                if current.value > max:
                    max = current.value
                current = current.next
            return max