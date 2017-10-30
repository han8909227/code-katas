
class Node(object):
    """Node Classs."""

    def __init__(self, data=None, next_data=None):
        """Initialize a new Node."""
        self.data = data
        self.next = next_data


class Stack(object):
    """Stack data strcuture."""

    def __init__(self, iterable=None):
        """Initialize a new instance of Stack."""
        self.top_stack = None
        self.count = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, new_stack):
        """Push value into the stack."""
        current = self.top_stack
        self.top_stack = Node(new_stack, current)
        self.count += 1

    def pop(self):
        """Pop out the top stack value."""
        if self.top_stack:
            result = self.top_stack.data
            if self.top_stack.next:
                self.top_stack = self.top_stack.next
            else:
                self.top_stack = None
            self.count -= 1
            return result
        else:
            raise ValueError('No value to pop')

    def __len__(self):
        """Return the size of the stack."""
        return self.count


def paren(s):
    """Check for valid paren combos."""
    l = Stack()
    for p in s:
        l.push(p)
    count = 0
    for p in range(len(l)):
        x = l.pop()
        if x == ')':
            count += 1
        elif x == '(':
            if count == 0:
                return 1
            else:
                count -= 1

    if count == 0:
        return 0
    else:
        return -1
