class Node:
    def __init__(self,payload = None):
        self.payload = payload
        self.next = None
        
class Fifo:
    def __init__(self, max_lenght = 10):
        self.head = Node()
        self.next = None
        self.max_lenght = max_lenght
        
    def append(self,payload):
        if self.is_full():
            print ('List is full')
            return None
        
        if type(payload).__name__!='int':
            print("Must be a intenger")
            return None
        
        if payload <= 0:
            print("Must be positive (>0)")
            return None
            
        new_node = Node(payload)
        current = self.head
        
        while current.next is not None:
            current = current.next
            
        current.next = new_node
    
    def lenght(self):
        current = self.head
        len = 0
        
        while current.next is not None:
            len += 1
            current = current.next
        
        return len
    
    def is_empty(self):
        if self.lenght() == 0:
            return True
        else:
            return False
            
                
    def is_full(self):
        if self.lenght() == self.max_lenght:
            return True
        else:
            return False
            
    def display(self):
        array = []
        current = self.head
        
        while current.next is not None:
            current = current.next
            array.append(current.payload)
        
        print(array)

    def pop(self):
        current = self.head
        self.head = current.next
        return current.next.payload


    
        
    
def main():
    list = Fifo()
    for number in range(11):
        list.append(number)
        
    while not list.is_empty():
        number = list.pop()

        if number %2 == 0:
            print(number)

    # print('Removed:' + str(list.pop()))
    list.display()


        
if __name__ == "__main__":
    main()
