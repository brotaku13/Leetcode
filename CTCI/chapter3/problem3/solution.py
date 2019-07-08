class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0
    
    def pop(self):
        if len(self.arr) == 0:
            raise Exception
        else:
            return self.arr.pop(-1)

    def has_room(self):
        return len(self.arr) < self.capacity
    
    def push(self, item):
        if capacity > 0:
            if len(self.arr) < self.capacity:
                self.arr.append(item)
            else:
                raise Exception
        else:
            self.arr.append(item)
    
    def top(self):
        if len(self.arr) == 0:
            raise Exception
        else:
            return self.arr[-1]


class SetOfStacks():

    def __init__(self, capacity):
        self.inner_capacity = capacity
        self.stacks = Stack(-1)
        
    def isEmpty(self):
        return self.stacks.isEmpty()
    
    def top(self):
        return self.stacks.top().top()
    
    def push(self, item):
        if len(self.stacks) == 0:
            self.stacks.push(Stack(self.inner_capacity))
        
        if not self.stacks.top().has_room():
            self.stacks.push(Stack(self.inner_capacity))

        self.stacks.top().push(item)
    
    def pop(self):
        if len(self.stacks) == 0:
            raise Exception
        
        value = self.top().pop()
        if self.top().isEmpty():
            self.stacks.pop()
        return value