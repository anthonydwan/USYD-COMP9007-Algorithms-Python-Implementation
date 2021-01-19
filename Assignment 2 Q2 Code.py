class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        self.MIN = None
        self.MAX = None
        self.AVG = None

    def insert_first(self, val):
        newNode = Node(val)
        #update size first to avoid confusion later on
        self.length +=1
        if self.head == None:
            #storing node
            self.head = newNode

            #updating variables
            self.MIN = newNode.val
            self.MAX = newNode.val
            self.AVG = newNode.val
        else:
            #storing the node in the list
            newNode.next = self.head
            self.head = newNode

            #updating all the variables
            if newNode.val < self.MIN:
                self.MIN = newNode.val
            if newNode.val > self.MAX:
                self.MAX = newNode.val
            self.AVG = ((self.AVG*(self.length-1))+newNode.val)/self.length
        return self

    # Print the linked list
    def listprint(self):
        printval = self.head
        while printval != None:
              print(printval.val)
              printval = printval.next

    def get_min(self):
        print(f"getting min: {self.MIN}")

    def get_max(self):
        print(f"getting max: {self.MAX}")

    def get_avg(self):
        print(f"getting avg: {self.AVG}")



#testing the code
eg = SLinkedList()
eg.insert_first(23)
eg.insert_first(46)
eg.insert_first(-2000)
eg.insert_first(678)
eg.insert_first(123)
eg.insert_first(867)
eg.insert_first(897)
eg.insert_first(53)
eg.insert_first(12)
eg.insert_first(74)
eg.listprint()
eg.get_min()
eg.get_max()
eg.get_avg()