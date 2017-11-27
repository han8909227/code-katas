"""Priority Queue data strcture."""


class Priorityq:
    """Priority Que class."""

    def __init__(self, value=None, pri=0):
        """Create a instance of the priority class."""
        self.q = {}

    def insert(self, data, pri=0):
        """Will insert a value in the priority queue with a priority of 0 or the optional priority input."""
        from que_ import Queue
        if not data:
            raise ValueError('need value to push')
        try:
            self.q[pri]
        except KeyError:
            self.q[pri] = Queue()
        self.q[pri].enqueue(data)

    def pop(self):
        """Will pop the first inserted instances of the highest priority and return the value."""
        if self.q == {}:
            raise ValueError('need value to pop')
        pri_to_pop = sorted(self.q.keys())[-1]
        q_pop = self.q[pri_to_pop].dequeue()
        try:
            self.q[pri_to_pop].peek()
        except AttributeError:
            del self.q[pri_to_pop]
        return q_pop

    def peek(self):
        """Return the next priority item that will be popped without popping the item."""
        if self.q == {}:
            raise ValueError('no values available')
        pri_to_peek = sorted(self.q.keys())[-1]
        return self.q[pri_to_peek].peek()

card_order = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}


def sort_cards(cards):
    """Sort the cards being inputted."""
    q = Priorityq()
    for card in cards:
        try:
            q.insert(card, card_order[card])
        except KeyError:
            raise ValueError('card value(s) must be part of the deck')
    result = [q.pop() for card in range(len(q.q))][::-1]
    return result

