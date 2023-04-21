from os import system

system("clear")


# ***  Doubly Linked Lists

print()

# * Doubly Linked Lists

"""

Objectives:

Understand the differences between singly linked lists and doubly linked lists
Understand the pros and cons of each
Construct a doubly linked list using OOP

Disclaimer: If you're ahead and have already finished all the mandatory assignments, please work on this assignments before moving on to Flask. 

Many students mention how they were expected to do linked list on the whiteboard during their technical interviews. 

If you're on schedule or not so ahead, you can skip this assignment and come back when you have more time.

These exercises are designed to help you prepare for technical interviews and to reinforce concepts you've learned about OOP. 
If you want to be better prepared for technical interviews, it's helpful to know linked lists and how they are used. 
Some interesting puzzles can be solved using linked lists 
(and you may be asked to solve problems using linked lists in technical interviews).

In technical interviews, our alumni are commonly asked problems involving linked lists. 

Learn about doubly-linked lists, also known as DLists. 
We started with singly-linked lists because they are simpler, 
but here's an opportunity to stretch your understanding and learn more by researching doubly-linked lists.


Once you have learned about linked lists, build a class in Python and demonstrate how you can:

    - add a new node to the end of the list,
    - delete an existing node,
    - insert a node between existing nodes (eg. before a given value, at a certain index, etc.)

You should have two classes for this: DoublyLinkedList and Node. 
Have DoublyLinkedList be the class that allows you to add a new node, 
delete an existing node, insert a new node between existing nodes, 
print out the values in the linked list. 

Have Node be the class that has the necessary properties for the node.

Please also think about the following:

How would you know if you have a circular linked list? -- Hint: you can use a runner technique to solve this problem.
How would you get to the middle of the linked list?
How would you remove duplicate values in the list?
How would you reverse the values in the list?
Think hard about these puzzles and how you could potentially use multiple runners to tackle some of these tasks.

Spend up to 5 hours on this assignment.

"""


class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display_all_values(self):
        if self.head == None:
            print("The list is empty")
            return self

        runner = self.head
        print("Displaying all values in the list:\n")
        print(f"Head: {self.head.value}")
        while runner != None:
            print(runner.value)
            runner = runner.next

        print(f"Tail: {self.tail.value}")
        print()
        return self

    def display_length(self):
        if self.head == None:
            print("The list is empty")
            return self
        if self.length == 1:
            print(f"There is {self.length} node in the list")
            return self
        print(f"There {self.length} nodes in the list")
        return self

    def display_head(self):
        if self.head == None:
            print("The list is empty")
            return self
        print(f"Head: {self.head.value}")
        return self

    def display_tail(self):
        if self.head == None:
            print("The list is empty")
            return self
        print(f"Tail: {self.tail.value}")
        return self

    def add_to_front(self, val):
        # Create new node
        new_node = DLNode(val)

        # if list is empty then set head and tail to new node and add 1 to length
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            print(f"--- Added {val} to the front of the list\n")
            return self

        # if list is not empty then set new node's next to head and set head's prev to new node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

        print(f"--- Added {val} to the front of the list\n")
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = DLNode(val)
        self.tail.next = new_node
        self.tail = new_node
        print(f"--- Added {val} to the back of the list\n")
        self.length += 1
        return self

    def insert_at(self, val, n):
        if n < 0:
            print("*** Invalid index, adding to front of list\n")
            self.add_to_front(val)
            return self
        if n == 0:
            self.add_to_front(val)
            return self
        if n >= self.length:
            print(
                "*** Invalid, Index is greater than the list length, adding to back of list\n"
            )
            self.add_to_back(val)
            return self
        new_node = DLNode(val)
        runner = self.head
        walker = self.head
        while n > 0:
            walker = runner
            runner = runner.next
            n -= 1

        walker.next = new_node
        new_node.prev = walker
        runner.prev = new_node
        new_node.next = runner

        self.length += 1
        print(f"--- Added {val} to the list at index {n}\n")
        return self

    def remove_from_front(self):
        if self.head == None:
            print("The list is empty\n")
            return self

        if self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            print("Removed the only node in the list\n")
            return self

        runner = self.head.next
        self.head.next = None
        runner.prev = None
        self.head = runner

        self.length -= 1
        print("Removed the first node in the list\n")
        return self

    def remove_from_back(self):
        if self.head == None:
            print("The list is empty\n")
            return self

        if self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            print("Removed the only node in the list\n")
            return self

        runner = self.head
        walker = self.head
        while runner.next != None:
            walker = runner
            runner = runner.next

        walker.next = None
        runner.prev = None
        self.tail = walker

        print("Removed the last node in the list\n")
        self.length -= 1
        return self

    def remove_at(self, n):
        index = n
        if self.head == None:
            print("The list is empty\n")
            return self
        if n < 0:
            print("*** Invalid index, removing from front of list\n")
            self.remove_from_front()
            return self
        if n == 0:
            self.remove_from_front()
            return self
        if n >= self.length:
            print(
                "*** Invalid, Index is greater than the list length, removing from back of list\n"
            )
            self.remove_from_back()
            return self
        if n == self.length - 1:
            self.remove_from_back()
            return self
        if n == self.length:
            print("Invalid index, removing from back of list\n")
            self.remove_from_back()
            return self

        runner = self.head
        walker = self.head
        while n > 0:
            walker = runner
            runner = runner.next
            n -= 1

        walker.next = runner.next
        runner.next.prev = walker
        runner.next = None
        runner.prev = None

        self.length -= 1
        print(f"--- Removed node at index {index}\n")
        return self

    def search(self, val):
        if self.head == None:
            print("The list is empty\n")
            return self

        runner = self.head
        while runner != None:
            if runner.value == val:
                print(f"Found {val} in the list\n")
                return self
            runner = runner.next

        print(f"{val} is not in the list\n")
        return self


my_list = DLList()

my_list.add_to_back(
    10
).display_all_values().display_length().display_head().display_tail()
print()
my_list.add_to_back(
    15
).display_all_values().display_length().display_head().display_tail()
print()
my_list.add_to_back(
    7
).display_all_values().display_length().display_head().display_tail()
print()
my_list.add_to_back(
    8
).display_all_values().display_length().display_head().display_tail()
print()
my_list.add_to_back(
    "Kim"
).display_all_values().display_length().display_head().display_tail()
print()
my_list.add_to_back(
    256
).display_all_values().display_length().display_head().display_tail()
print()
my_list.insert_at(
    12, 2
).display_all_values().display_length().display_head().display_tail()
print()
my_list.insert_at(
    35, 1
).display_all_values().display_length().display_head().display_tail()
print()
# my_list.remove_from_front().display_all_values().display_length().display_head().display_tail()
# print()
# my_list.remove_from_front().display_all_values().display_length().display_head().display_tail()
# print()
# my_list.remove_from_back().display_all_values().display_length().display_head().display_tail()
# print()
# my_list.remove_from_back().display_all_values().display_length().display_head().display_tail()
# print()
my_list.remove_at(8).display_all_values().display_length().display_head().display_tail()
print()
my_list.search(
    "Cragar"
).display_all_values().display_length().display_head().display_tail()

#
#
print()
