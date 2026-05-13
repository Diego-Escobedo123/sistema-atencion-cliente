'''
Ticket model.
'''


class Ticket:
    def __init__(self, ticket_id, client, description, priority):
        self.ticket_id = ticket_id
        self.client = client
        self.description = description
        self.priority = priority
        self.next = None

    def __repr__(self):
        return f'[{self.ticket_id}] {self.client} | Priority: {self.priority} | {self.description}'

    def to_dict(self):
        labels = {1: 'Critical', 2: 'High', 3: 'Medium', 4: 'Low'}
        return {
            'ticket_id': self.ticket_id,
            'client': self.client,
            'description': self.description,
            'priority': self.priority,
            'priority_label': labels[self.priority]
        }