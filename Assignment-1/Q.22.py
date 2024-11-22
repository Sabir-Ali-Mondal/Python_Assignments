class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} into the queue.")

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.queue.pop(0)
            print(f"Dequeued {dequeued_item} from the queue.")
            return dequeued_item
        else:
            print("Queue is empty. Cannot dequeue any element.")
            return None

    def front(self):
        if not self.is_empty():
            front_item = self.queue[0]
            print(f"Front element is {front_item}.")
            return front_item
        else:
            print("Queue is empty. No front element.")
            return None

    def size(self):
        current_size = len(self.queue)
        print(f"Current queue size: {current_size}")
        return current_size

    def display(self):
        if not self.is_empty():
            print("Queue elements are:")
            for item in self.queue:
                print(item)
        else:
            print("Queue is empty. Nothing to display.")

# Example usage
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

queue.front()

queue.dequeue()
queue.display()

queue.size()
