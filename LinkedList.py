class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, value: int) -> None:
        """Adds a new node with the given value to the end of the LinkedList.

        Parameters:
        -----------
        value (int): The value to be added to the LinkedList.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp.next is not None:
                temp =temp.next
            temp.next = new_node
                

    def find(self, value: int) -> int:
        """find the value of our LinkedList

        Parameters:
        -----------
        value(int)

        returns int

        """

        temp = self.root
        index = 0
        while temp is not None:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return -1


    def get(self, index: int) -> int:
        """get the index of our LinkedList
        Parameters:
        -----------
        inxed(int)

        returns int
        """   
        temp = self.root
        i = 0
        while temp is not None:
            if i == index:
                return temp.value
            i += 1
            temp = temp.next
        return -1 

            


    def insert(self, index: int, value: int) -> None:
        """ add anywhere
        Parameters
        ------------
        index(int)
        values(int)
        """
        new_node = Node(value)
        if index == 0:
            new_node.next = self.root
            self.root = new_node
        temp =self.root
        i = 0
        while temp is not None:
            if i == index:
                new_node.next = temp
                previous.next = new_node
                return
            i += 1
            previous = temp
            temp = temp.next


    def delete(self, index: int) -> None:
        """delete our LinkedList
        Parameters
        ------------
        index(int
        """

        temp = self.root
        i = 0
        while temp is not None:
            if i == index:
                previous.next = temp.next
                return
            i += 1
            previous = temp
            temp = temp.next
    

    def print_list(self):
        """Prints the values in the LinkedList."""
        temp = self.root
        while temp is not None:
            print(temp.value, end=" , ")
            temp = temp.next
        print("None")


# Example usage
my_ls = LinkedList()
print(1)
my_ls.add(30)#0
print(2)
my_ls.add(40)#1
print(3)
my_ls.add(50)#2
my_ls.print_list() 

print(my_ls.find(40))
print(my_ls.get(1))
my_ls.insert(1,90)
my_ls.print_list()

my_ls.delete(1)
print('new')
my_ls.print_list()