'''
Helpdesk manager.
'''

from priority_queue import PriorityQueue

class Helpdesk:
    def __init__(self):
        self.queue = PriorityQueue()
        self.history = []

    def add_ticket(self, client, description, priority):
        node = self.queue.insert(client, description, priority)
        return node

    def attend_next(self):
        node = self.queue.delete()
        if node is None:
            return None
        self.history.append(node.to_dict())
        return node

    def search_ticket(self, ticket_id):
        return self.queue.search(ticket_id)

    def update_priority(self, ticket_id, new_priority):
        return self.queue.update_priority(ticket_id, new_priority)

    def get_tickets(self):
        tickets = []
        current = self.queue.start
        while current is not None:
            tickets.append(current.to_dict())
            current = current.next
        return tickets

    def get_history(self):
        return self.history

    def get_total(self):
        return len(self.queue)