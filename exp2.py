# implement data structure
#stack
#queue
#linked list

#code for stack
print("Stack");
class Stack:
    def __init__(self):
        self.stack = [];
    def push(self,element):
        self.stack.append(element);
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop();
        else:
            return "Stack is empty";
    def display(self):
        print(self.stack);

stack1 = Stack();
stack1.push(1);
stack1.push(2);
stack1.push(3);
stack1.display();

#queue 
print("Queue");
class Queue:
    def __init__(self):
        self.queue = [];
    def enqueue(self,element):
        self.queue.append(element);
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0);
        else:
            return "Queue is empty";
    def display(self):
        print(self.queue);

queue1 = Queue();
queue1.enqueue(1);
queue1.enqueue(2);
queue1.enqueue(3);
queue1.display();




#linked list
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

# linked list
print("Linked list");
class LinkedList:
    def __init__(self):
        self.head = None;
    def add(self,data):
        if self.head == None:
            self.head = Node(data);
        else:
            temp = self.head;
            while temp.next != None:
                temp = temp.next;
            temp.next = Node(data);
    def display(self):
        temp = self.head;
        while temp != None:
            print(temp.data);
            temp = temp.next;

linkedList1 = LinkedList();
linkedList1.add(1);
linkedList1.add(2);
linkedList1.add(3);
linkedList1.display();

