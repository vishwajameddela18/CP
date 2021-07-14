"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        print(self.storage)
        

    def peek(self):
        return self.storage[0]
        

    def dequeue(self):
        print(self.storage)
        if self.storage != []:
            return self.storage.pop(0)
            
        # return self.storage
        
        