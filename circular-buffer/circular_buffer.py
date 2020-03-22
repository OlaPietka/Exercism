class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if self.buffer is []:
            raise ValueError("Buffer is empty")
        return self.buffer.pop(0)

    def write(self, data):
        if self.is_full():
            raise ValueError("Buffer is full")
        self.buffer.append(data)

    def overwrite(self, data):
        if self.is_full():
            self.read()
        self.write(data)

    def clear(self):
        self.buffer = []

    def is_full(self):
        return len(self.buffer) == self.capacity
