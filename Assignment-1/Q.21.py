class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Stack is empty. Cannot pop any element.")
            return None

    def peek(self):
        if not self.is_empty():
            top_item = self.stack[-1]
            print(f"Top element is {top_item}.")
            return top_item
        else:
            print("Stack is empty. No top element.")
            return None

    def size(self):
        current_size = len(self.stack)
        print(f"Current stack size: {current_size}")
        return current_size

    def display(self):
        if not self.is_empty():
            print("Stack elements are:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty. Nothing to display.")

# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

stack.peek()

stack.pop()
stack.display()

stack.size()
