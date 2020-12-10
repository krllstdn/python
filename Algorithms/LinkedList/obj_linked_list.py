# 1. Základní strukturou je Prvek, obsahující data (int) a ukazatel na další prvek v pořadí. 
#    Struktura Seznam pak obsahuje ukazatel na první prvek (hlava) a poslední prvek (zarážka).
# 2. Korektní založení a vymazání seznamu, přidání prvku na konec a začátek.
# 3. Vypsání seznamu prvek po prvku, nalezení nejmenšího a největšího prvku.
# 4. Seřazení seznamu od nejmenšího/největšího prvku.

class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # prints out linked list
    def print_list(self):
        print_val = self.head
        while print_val is not None: # print while there is what to print
            print(print_val.val)
            print_val = print_val.next
    

    # adds the node to the end
    def add_to_the_end(self, value):
        new_node = Node(value)

        if self.head is None: # in case there are no nodes
            self.head = new_node
            return True # exit the method

        # getting the last node
        last_node = self.head
        while(last_node.next): 
            last_node = last_node.next
        last_node.next = new_node # assigning the link to the new node

    # adds node to the beginnig of the linked list
    def add_to_the_begginning(self, value):
        new_node = Node(value)
        
        if self.head is None: # in case there are no nodes
            self.head = new_node
            return True # exit the method
        
        new_node.next = self.head # add the link to the next node
        self.head = new_node # change the self.head value
    
  
    # deletes node
    def node_delete(self, del_node): 
        head = self.head

        if head is not None: # if the list isn't empty
            if head.val == del_node: # if the first node is the node we want to delete
                self.head = head.next # rearrange the head in the list
                head = None # delete former head
                return True # exit the function

        
        while head is not None: # look through all the nodes to find the sought
            if head.val == del_node: 
                break
            prev = head
            head = head.next

        if head == None: # exit function if the the node've been deleted
            return True
        
        prev.next = head.next

        head = None

    # accepts value and returns object.
    # used in inserting between nodes
    def get_node_obj(self, node_value):
        headval = self.head

        while headval.val != node_value:
            headval = headval.next

        return headval
    
    # inserts node between two existing nodes
    def insert_in_between(self, middle_node, value):
        if middle_node is None:
            print("Invalid node value")
            return False

        middle_node = self.get_node_obj(middle_node)

        node = Node(value)
        node.next = middle_node.next
        middle_node.next = node

    # converts linked list in usual list
    # used in sorting
    def get_the_nodes(self):
        list_values = []

        node_val = self.head

        while node_val is not None:
            list_values.append(node_val.val)
            node_val = node_val.next
        return list_values

    #finds the biggest value
    def find_the_biggest(self, list_values):
        # loop through the L.L.
        # create a list with values
        # loop through a list to find the biggest

        max = list_values[0]
        for i in range(0, len(list_values)):
            if list_values[i] > max:
                max = list_values[i]

        return max

    #finds the lowest value
    def find_the_lowest(self, list_values):
        min = list_values[0]
        for i in range(0, len(list_values)):
            if list_values[i] < min:
                min = list_values[i]

        return min


    def sort_biggest_to_lowest(self):
    # loop though all the values
    # with each iteration add the biggest value from the value list 
    #  to new list and delete that value from the former

        list_values = self.get_the_nodes()
        sorted = []

        while list_values:
            biggest = self.find_the_biggest(list_values)
            sorted.append(biggest)
            list_values.remove(biggest)
        self.list_to_linked_list(sorted)

        return sorted


    def sort_lowest_to_biggest(self):
    # loop though all the values
    # with each iteration add the lowest value from the value list 
    #  to new list and delete that value from the former
        list_values = self.get_the_nodes()
        sorted = []

        while list_values:
            biggest = self.find_the_lowest(list_values)
            sorted.append(biggest)
            list_values.remove(biggest)
        self.list_to_linked_list(sorted)

        return sorted

    # converts usual list to linked list
    # used in sorting
    def list_to_linked_list(self, list):
        # clear the linked list
        head = self.head
        while head is not None:
            prev = head
            head.next = None
            head.val = None
            head = prev.next           
        # add the values into the linked list
        for i in range(0, len(list)):               
            self.add_to_the_end(list[i])

        
llist = LinkedList()

llist.head = Node(23) #the node

n2 = Node(4)

n3 = Node(34)

llist.head.next = n2 # the link to the next node
n2.next = n3 # the link to the next node

llist.add_to_the_begginning(34)
llist.add_to_the_begginning(56)
llist.add_to_the_end(45646)
llist.insert_in_between(23, 789)



llist.sort_biggest_to_lowest()

llist.print_list()


llist.sort_lowest_to_biggest()











    
