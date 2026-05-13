'''
Priority Queue implementation using a sorted linked list.
'''

from ticket import Ticket


class PriorityQueue:
    def __init__(self):
        self.start = None
        self._counter = 0

    def __repr__(self):
        nodes = ['START']
        current = self.start
        while current is not None:
            nodes.append(str(current))
            current = current.next
        nodes.append('NIL')
        return '\n' + ' --> \n'.join(nodes)

    def __len__(self):
        count = 0
        current = self.start
        while current is not None:
            count += 1
            current = current.next
        return count

    # insert - O(n)
    def insert(self, client, description, priority):
        self._counter += 1
        ticket_id = f'TKT-{self._counter:04d}'
        new_node = Ticket(ticket_id, client, description, priority)

        if self.start is None or priority < self.start.priority:
            new_node.next = self.start
            self.start = new_node
        else:
            current = self.start
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        return new_node

    # delete - O(1)
    def delete(self):
        if self.start is None:
            print('Queue underflow')
            return None

        removed = self.start
        self.start = self.start.next
        removed.next = None
        return removed

    # search - O(n)
    def search(self, ticket_id):
        current = self.start
        while current is not None:
            if current.ticket_id == ticket_id:
                return current
            current = current.next
        return None

    # update_priority - O(n)
    def update_priority(self, ticket_id, new_priority):
        current = self.start
        prev = None

        while current is not None:
            if current.ticket_id == ticket_id:
                # Remove from current position
                if prev is None:
                    self.start = current.next
                else:
                    prev.next = current.next
                current.next = None

                # Re-insert with new priority
                current.priority = new_priority
                if self.start is None or new_priority < self.start.priority:
                    current.next = self.start
                    self.start = current
                else:
                    p = self.start
                    while p.next is not None and p.next.priority <= new_priority:
                        p = p.next
                    current.next = p.next
                    p.next = current

                return current
            prev = current
            current = current.next

        return None

    # is_empty - O(1)
    def is_empty(self):
        return self.start is None

    # peek - O(1)
    def peek(self):
        return self.start